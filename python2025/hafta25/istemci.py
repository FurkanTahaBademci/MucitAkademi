# ============================================================
#  HAFTA 25 - CANLI ANONİM DUVAR: KOMUTSATIRı İSTEMCİSİ
# ============================================================
#
#  Bu dosya ÖĞRENCİLERİN bilgisayarında çalışır.
#  Grafiksel arayüz istemeyenler için basit terminal versiyonu.
#
#  ÇALIŞTIRMAK:
#    python istemci.py
#
#  Sunucu IP'sini komut satırından da verebilirsin:
#    python istemci.py --ip 192.168.1.10
#
# ============================================================

import urllib.request
import urllib.error
import json
import sys

# -----------------------------------------------------------
# AYARLAR
# -----------------------------------------------------------

VARSAYILAN_IP = "127.0.0.1"
PORT = 5000

# Komut satırı argümanı: python istemci.py --ip 192.168.1.5
if "--ip" in sys.argv:
    idx = sys.argv.index("--ip")
    if idx + 1 < len(sys.argv):
        VARSAYILAN_IP = sys.argv[idx + 1]

SUNUCU_URL = f"http://{VARSAYILAN_IP}:{PORT}"

# -----------------------------------------------------------
# YARDIMCI FONKSİYONLAR
# -----------------------------------------------------------

def mesaj_gonder(ad, mesaj):
    """Sunucuya POST isteği gönderir."""
    veri = json.dumps({"ad": ad, "mesaj": mesaj}).encode("utf-8")
    istek = urllib.request.Request(
        url=f"{SUNUCU_URL}/mesaj",
        data=veri,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(istek, timeout=5) as yanit:
            yanit_veri = json.loads(yanit.read().decode())
            return True, yanit_veri
    except urllib.error.HTTPError as e:
        try:
            hata = json.loads(e.read().decode())
            return False, hata.get("hata", f"HTTP {e.code}")
        except Exception:
            return False, f"HTTP Hatası: {e.code}"
    except urllib.error.URLError:
        return False, "Sunucuya bağlanılamadı! IP adresini kontrol et."
    except Exception as e:
        return False, str(e)


def mesajlari_listele():
    """Sunucudaki tüm mesajları çekip ekrana yazar."""
    try:
        with urllib.request.urlopen(f"{SUNUCU_URL}/mesajlar", timeout=5) as yanit:
            veri = json.loads(yanit.read().decode())
            mesajlar = veri.get("mesajlar", [])
            if not mesajlar:
                print("  (Henüz mesaj yok)")
                return
            print(f"\n  Toplam {len(mesajlar)} mesaj:")
            print("  " + "-" * 50)
            for m in mesajlar:
                print(f"  [{m['zaman']}] {m['ad']}: {m['mesaj']}")
            print("  " + "-" * 50)
    except Exception as e:
        print(f"  Hata: {e}")


# -----------------------------------------------------------
# ANA MENÜ
# -----------------------------------------------------------

def ana_menu():
    print("=" * 55)
    print("  📌 ANONİM DUVAR - KOMUT SATIRI İSTEMCİSİ")
    print("=" * 55)
    print(f"  Sunucu: {SUNUCU_URL}")
    print("=" * 55)

    while True:
        print("\n  Ne yapmak istersin?")
        print("  [1] Mesaj gönder")
        print("  [2] Tüm mesajları gör")
        print("  [3] Çıkış")
        print()

        secim = input("  Seçimin (1/2/3): ").strip()

        if secim == "1":
            print()
            ad = input("  Adın veya takma adın (boş bırakırsan 'Anonim'): ").strip()
            if not ad:
                ad = "Anonim"
            mesaj = input("  Mesajın: ").strip()
            if not mesaj:
                print("  ⚠️  Mesaj boş olamaz!")
                continue

            print("  Gönderiliyor...")
            basari, sonuc = mesaj_gonder(ad, mesaj)
            if basari:
                print(f"  ✅  Mesajın duvara eklendi!")
            else:
                print(f"  ❌  Hata: {sonuc}")

        elif secim == "2":
            mesajlari_listele()

        elif secim == "3":
            print("  Görüşürüz! 👋")
            break

        else:
            print("  ⚠️  Geçersiz seçim. 1, 2 veya 3 gir.")


# -----------------------------------------------------------
# BAŞLAT
# -----------------------------------------------------------

if __name__ == "__main__":
    ana_menu()
