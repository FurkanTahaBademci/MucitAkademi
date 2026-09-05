# ============================================================
#  LAN SOHBET UYGULAMASI - TERMİNAL İSTEMCİ
# ============================================================
#
#  Bu dosyayı sunucuya bağlanmak isteyen HER bilgisayar çalıştırır.
#  (Sunucu olan bilgisayar da bunu çalıştırabilir)
#
#  ÇALIŞTIRMAK:
#    python istemci.py
#
#  Program senden şunları isteyecek:
#    1. Sunucunun IP adresi  (sunucu.py çalışan bilgisayarın IP'si)
#    2. Port                 (varsayılan: 5555)
#    3. Kullanıcı adın
#
#  Bağlandıktan sonra mesaj yazıp Enter'a bas.
#  Çıkmak için: "çık" yaz ve Enter'a bas.
#
# ============================================================

import socket
import threading
import sys

# -----------------------------------------------------------
# MESAJ AL: Arka planda sürekli sunucudan mesaj dinler
# -----------------------------------------------------------

def mesaj_al(sunucu_socket):
    """
    Bu fonksiyon ayrı bir thread'de çalışır.
    Sürekli sunucudan gelen mesajları ekrana yazar.
    Bağlantı kopunca durur.
    """
    while True:
        try:
            veri = sunucu_socket.recv(2048)
            if not veri:
                print("\n[!] Sunucu bağlantıyı kapattı.")
                break

            mesaj = veri.decode("utf-8")
            # Gelen mesajı mevcut satırın üstüne güzel yaz
            print(mesaj, end="", flush=True)

        except ConnectionResetError:
            print("\n[!] Sunucuyla bağlantı kesildi.")
            break
        except Exception as e:
            if "10054" in str(e) or "10053" in str(e):   # Windows bağlantı hataları
                print("\n[!] Bağlantı koptu.")
            break

    # Thread bitince programı kapat
    sys.exit(0)

# -----------------------------------------------------------
# BAĞLAN
# -----------------------------------------------------------

def baglan():
    print("=" * 50)
    print("  LAN SOHBET - TERMİNAL İSTEMCİ")
    print("=" * 50)
    print()

    # Sunucu IP
    ip = input("Sunucu IP adresi [varsayılan: 127.0.0.1]: ").strip()
    if not ip:
        ip = "127.0.0.1"

    # Port
    port_str = input("Port [varsayılan: 5555]: ").strip()
    port = int(port_str) if port_str.isdigit() else 5555

    # Kullanıcı adı
    while True:
        nickname = input("Kullanıcı adın: ").strip()
        if nickname:
            break
        print("[!] Kullanıcı adı boş olamaz!")

    print()
    print(f"[*] {ip}:{port} adresine bağlanılıyor...")

    # Socket oluştur ve bağlan
    try:
        sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sunucu.connect((ip, port))
    except ConnectionRefusedError:
        print("[X] Bağlantı reddedildi!")
        print("    → Sunucu çalışıyor mu? IP ve port doğru mu?")
        input("\nÇıkmak için Enter...")
        return
    except OSError as e:
        print(f"[X] Bağlantı hatası: {e}")
        input("\nÇıkmak için Enter...")
        return

    # Sunucu nickname istiyor
    try:
        istek = sunucu.recv(1024).decode("utf-8")
        if istek == "NICK?":
            sunucu.send(nickname.encode("utf-8"))
    except Exception as e:
        print(f"[X] Protokol hatası: {e}")
        return

    print(f"[✓] Bağlandı! Hoş geldin, {nickname}!")
    print(f"    Çıkmak için 'çık' yaz.\n")
    print("-" * 50)

    # Mesaj alma thread'ini başlat (arka planda çalışır)
    al_thread = threading.Thread(target=mesaj_al, args=(sunucu,), daemon=True)
    al_thread.start()

    # Ana döngü: Mesaj gönder
    try:
        while True:
            mesaj = input()   # Kullanıcı bir şey yazıp Enter'a basana kadar bekle

            if mesaj.strip().lower() in ("çık", "cik", "exit", "quit", "q"):
                print("[*] Sohbetten ayrılıyorsunuz...")
                break

            if not mesaj.strip():
                continue   # Boş mesaj gönderme

            try:
                sunucu.send(mesaj.encode("utf-8"))
            except Exception:
                print("[!] Mesaj gönderilemedi. Bağlantı kopmuş olabilir.")
                break

    except KeyboardInterrupt:
        print("\n[*] Çıkılıyor...")

    finally:
        sunucu.close()

# -----------------------------------------------------------

if __name__ == "__main__":
    baglan()
