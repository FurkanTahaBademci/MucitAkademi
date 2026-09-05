# ============================================================
#  LAN SOHBET UYGULAMASI - SUNUCU
# ============================================================
#
#  Bu dosya sunucudur. Sadece BİR bilgisayarda çalışır.
#  Diğer bilgisayarlar istemci.py veya istemci_gui.py ile bağlanır.
#
#  ÇALIŞTIRMAK:
#    python sunucu.py
#
#  Sunucu başlayınca ekrana IP adresini yazar.
#  O IP'yi arkadaşlarına söyle, onlar istemci'ye girecek.
#
# ------------------------------------------------------------
#  NASIL ÇALIŞIR?
#
#  [Bilgisayar A - Sunucu]          [Bilgisayar B - İstemci]
#       sunucu.py ←────────────────── istemci.py
#            ↑                              ↑
#            └──────── [Bilgisayar C] ──────┘
#
#  Sunucu, gelen her mesajı TÜM istemcilere iletir.
#  Tıpkı bir WhatsApp grup yöneticisi gibi!
#
# ============================================================

import socket
import threading

# -----------------------------------------------------------
# AYARLAR
# -----------------------------------------------------------

HOST = "0.0.0.0"   # "0.0.0.0" = tüm ağ arayüzlerini dinle
PORT = 5555         # Bağlantı portu (1024-65535 arası herhangi biri)

# -----------------------------------------------------------
# GLOBAL DEĞİŞKENLER
# -----------------------------------------------------------

bagli_istemciler = []   # Bağlı socket nesneleri
kullanici_adlari  = []   # Her istemcinin kullanıcı adı
kilit = threading.Lock() # Aynı anda birden fazla thread listeye
                          # eriştiğinde karışıklık olmaması için

# -----------------------------------------------------------
# YARDIMCI: Yerel IP'yi bul
# -----------------------------------------------------------

def yerel_ip_bul():
    """Bilgisayarın yerel ağ (LAN) IP adresini döndürür"""
    try:
        # Dışarıya bağlanmaya çalışırız ama paket göndermeyiz
        # Sadece hangi ağ arayüzü kullanılacağını öğreniriz
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# -----------------------------------------------------------
# YAYINLA: Mesajı tüm istemcilere gönder
# -----------------------------------------------------------

def yayinla(mesaj_bytes, gonderici_socket=None):
    """
    Gelen mesajı bağlı herkese iletir.
    gonderici_socket = None ise sunucu mesajıdır, herkese gider.
    gonderici_socket verilmişse O kişi dahil herkese gider
    (istemci kendi mesajını sunucudan görsün ki ekranda uniform görünsün).
    """
    with kilit:
        kopya = bagli_istemciler[:]   # Listeyi kopyala (döngü sırasında değişebilir)

    for istemci in kopya:
        try:
            istemci.send(mesaj_bytes)
        except Exception:
            # Gönderim başarısız = istemci koptu, temizle
            istemci_cikar(istemci)

# -----------------------------------------------------------
# İSTEMCİ ÇIKAR: Listelerden sil
# -----------------------------------------------------------

def istemci_cikar(istemci_socket):
    """Bağlantısı kopan istemciyi listelerden çıkarır"""
    with kilit:
        if istemci_socket in bagli_istemciler:
            idx = bagli_istemciler.index(istemci_socket)
            bagli_istemciler.pop(idx)
            ad = kullanici_adlari.pop(idx)
        else:
            ad = "Bilinmeyen"
    try:
        istemci_socket.close()
    except Exception:
        pass
    return ad

# -----------------------------------------------------------
# İSTEMCİ YÖNET: Her istemci için ayrı thread'de çalışır
# -----------------------------------------------------------

def istemci_isle(istemci_socket, adres):
    """
    Tek bir istemciyle iletişimi yönetir.
    Her istemci için threading.Thread ile ayrı bir kopya çalışır.
    """

    try:
        # 1. Kullanıcı adı iste
        istemci_socket.send("NICK?".encode("utf-8"))
        nickname = istemci_socket.recv(1024).decode("utf-8").strip()

        if not nickname:
            istemci_socket.close()
            return

        # 2. Listeye ekle
        with kilit:
            kullanici_adlari.append(nickname)
            bagli_istemciler.append(istemci_socket)

        print(f"[+] {nickname} bağlandı  ({adres[0]}:{adres[1]})")
        print(f"    Şu an bağlı: {len(bagli_istemciler)} kişi")

        # 3. Herkese katılma bildirimi
        yayinla(f"\n  *** {nickname} sohbete katıldı! ***\n".encode("utf-8"))

        # 4. Mesajları dinle
        while True:
            try:
                veri = istemci_socket.recv(2048)
                if not veri:
                    break   # Bağlantı kapandı

                mesaj = veri.decode("utf-8").strip()
                if not mesaj:
                    continue

                tam_mesaj = f"[{nickname}]: {mesaj}"
                print(tam_mesaj)   # Sunucu konsoluna yaz

                # Herkese ilet (gönderici dahil - böylece herkes aynı formatı görür)
                yayinla(f"{tam_mesaj}\n".encode("utf-8"))

            except ConnectionResetError:
                break
            except Exception as e:
                print(f"[!] {nickname} hata: {e}")
                break

    finally:
        # 5. Bağlantı bitti - temizle ve bildir
        ad = istemci_cikar(istemci_socket)
        print(f"[-] {ad} ayrıldı  |  Kalan: {len(bagli_istemciler)} kişi")
        yayinla(f"\n  *** {ad} sohbetten ayrıldı. ***\n".encode("utf-8"))

# -----------------------------------------------------------
# ANA SUNUCU DÖNGÜSÜ
# -----------------------------------------------------------

def sunucuyu_baslat():
    sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SO_REUSEADDR: Sunucu yeniden başlatılınca "port meşgul" hatası almamak için
    sunucu.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sunucu.bind((HOST, PORT))
    sunucu.listen()

    yerel_ip = yerel_ip_bul()

    print("=" * 55)
    print("       LAN SOHBET SUNUCUSU BAŞLADI")
    print("=" * 55)
    print(f"  Yerel IP Adresin : {yerel_ip}")
    print(f"  Port             : {PORT}")
    print()
    print(f"  Arkadaşlarına şunu söyle:")
    print(f"  ► Sunucu IP: {yerel_ip}   Port: {PORT}")
    print()
    print("  Durdurmak için: Ctrl + C")
    print("=" * 55)
    print()

    try:
        while True:
            istemci_socket, adres = sunucu.accept()
            # Her istemci için yeni bir thread başlat
            # daemon=True → Ana program kapanınca bu thread de kapanır
            t = threading.Thread(
                target=istemci_isle,
                args=(istemci_socket, adres),
                daemon=True
            )
            t.start()

    except KeyboardInterrupt:
        print("\n[*] Sunucu kapatılıyor...")
    finally:
        sunucu.close()

# -----------------------------------------------------------

if __name__ == "__main__":
    sunucuyu_baslat()
