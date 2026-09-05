# ============================================================
#  HAFTA 25 - CANLI ANONİM DUVAR: CANLI EKRAN (Projektör)
# ============================================================
#
#  Bu dosya ÖĞRETMEN bilgisayarında çalışır.
#  sunucu.py ile AYNI ANDA çalıştırılır.
#  Gelen mesajları büyük ekranda / projektörde gösterir.
#
#  ÇALIŞTIRMAK:
#    python canli_duvar.py
#    (Sunucu IP'si otomatik algılanır: 127.0.0.1)
#
#  Uzak sunucu kullanmak istersen:
#    python canli_duvar.py --ip 192.168.1.10
#
# ============================================================

import tkinter as tk
import threading
import time
import sys
import urllib.request
import json

# -----------------------------------------------------------
# AYARLAR
# -----------------------------------------------------------

SUNUCU_IP   = "127.0.0.1"   # Komut satırından --ip ile değiştirilebilir
PORT        = 5000
YENILEME_MS = 2500           # Kaç ms'de bir mesajları çek (2.5 saniye)

# Komut satırı argümanı: python canli_duvar.py --ip 192.168.1.5
if "--ip" in sys.argv:
    idx = sys.argv.index("--ip")
    if idx + 1 < len(sys.argv):
        SUNUCU_IP = sys.argv[idx + 1]

SUNUCU_URL = f"http://{SUNUCU_IP}:{PORT}/mesajlar"

# Renkler (koyu tema, projektörde iyi görünür)
ARKAPLAN    = "#1a1a2e"
KART_RENK   = "#16213e"
BASLIK_RENK = "#e94560"
METIN_RENK  = "#eeeeee"
ZAMAN_RENK  = "#888888"
AD_RENK     = "#e94560"

# -----------------------------------------------------------
# VERİ ÇEKME (arka plan thread'i)
# -----------------------------------------------------------

son_mesaj_id = 0   # En son gördüğümüz mesajın ID'si

def mesajlari_cek():
    """Sunucudan mesaj listesini JSON olarak çeker."""
    try:
        with urllib.request.urlopen(SUNUCU_URL, timeout=3) as yanit:
            veri = json.loads(yanit.read().decode())
            return veri.get("mesajlar", [])
    except Exception:
        return None

# -----------------------------------------------------------
# TKİNTER ARAYÜZÜ
# -----------------------------------------------------------

class CanliDuvar:
    def __init__(self, kok):
        self.kok = kok
        self.kok.title("📌 Canlı Anonim Duvar")
        self.kok.configure(bg=ARKAPLAN)
        self.kok.attributes("-fullscreen", True)   # Tam ekran
        self.kok.bind("<Escape>", lambda e: self.kok.attributes("-fullscreen", False))
        self.kok.bind("<F11>",    lambda e: self.kok.attributes("-fullscreen", True))

        self._arayuz_kur()
        self._guncelle()

    # -------------------------------------------------------
    def _arayuz_kur(self):
        # Üst başlık
        ust = tk.Frame(self.kok, bg=ARKAPLAN)
        ust.pack(fill="x", padx=30, pady=(20, 0))

        tk.Label(
            ust, text="📌 Canlı Anonim Duvar",
            font=("Segoe UI", 28, "bold"),
            bg=ARKAPLAN, fg=BASLIK_RENK
        ).pack(side="left")

        self.sayac_etiketi = tk.Label(
            ust, text="0 mesaj",
            font=("Segoe UI", 14),
            bg=ARKAPLAN, fg=ZAMAN_RENK
        )
        self.sayac_etiketi.pack(side="right")

        self.durum_etiketi = tk.Label(
            self.kok, text=f"Sunucu: {SUNUCU_URL}",
            font=("Segoe UI", 10),
            bg=ARKAPLAN, fg=ZAMAN_RENK
        )
        self.durum_etiketi.pack(pady=(4, 12))

        # Kaydırılabilir mesaj alanı
        cerceve = tk.Frame(self.kok, bg=ARKAPLAN)
        cerceve.pack(fill="both", expand=True, padx=30, pady=(0, 20))

        self.canvas = tk.Canvas(cerceve, bg=ARKAPLAN, highlightthickness=0)
        kaydirici = tk.Scrollbar(cerceve, orient="vertical",
                                  command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=kaydirici.set)

        kaydirici.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.ic_cerceve = tk.Frame(self.canvas, bg=ARKAPLAN)
        self.canvas_pencere = self.canvas.create_window(
            (0, 0), window=self.ic_cerceve, anchor="nw"
        )
        self.ic_cerceve.bind("<Configure>", self._canvas_guncelle)
        self.canvas.bind("<Configure>", self._genislik_guncelle)

        # Fare tekerleği ile kaydırma
        self.canvas.bind_all("<MouseWheel>",
            lambda e: self.canvas.yview_scroll(-1 * (e.delta // 120), "units"))

    # -------------------------------------------------------
    def _canvas_guncelle(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _genislik_guncelle(self, event):
        self.canvas.itemconfig(self.canvas_pencere, width=event.width)

    # -------------------------------------------------------
    def _kart_ekle(self, ad, mesaj, zaman, yeni=False):
        """Tek bir mesaj kartı oluşturur."""
        kart = tk.Frame(
            self.ic_cerceve,
            bg=KART_RENK,
            bd=0,
            relief="flat",
            padx=18, pady=12
        )
        kart.pack(fill="x", padx=8, pady=6)

        # Sol kırmızı çizgi (görsel efekt için)
        cizgi = tk.Frame(kart, bg=BASLIK_RENK, width=4)
        cizgi.pack(side="left", fill="y", padx=(0, 14))

        icerik = tk.Frame(kart, bg=KART_RENK)
        icerik.pack(side="left", fill="both", expand=True)

        tk.Label(
            icerik, text=f"👤  {ad}",
            font=("Segoe UI", 13, "bold"),
            bg=KART_RENK, fg=AD_RENK,
            anchor="w"
        ).pack(fill="x")

        tk.Label(
            icerik, text=mesaj,
            font=("Segoe UI", 15),
            bg=KART_RENK, fg=METIN_RENK,
            anchor="w", wraplength=900, justify="left"
        ).pack(fill="x", pady=(4, 0))

        tk.Label(
            icerik, text=f"🕐 {zaman}",
            font=("Segoe UI", 10),
            bg=KART_RENK, fg=ZAMAN_RENK,
            anchor="w"
        ).pack(fill="x", pady=(4, 0))

    # -------------------------------------------------------
    def _guncelle(self):
        """Arka planda mesajları çeker, yenileri varsa ekler."""
        def is_yap():
            global son_mesaj_id
            mesajlar = mesajlari_cek()

            if mesajlar is None:
                self.kok.after(0, lambda: self.durum_etiketi.config(
                    text="⚠️  Sunucuya bağlanılamıyor...", fg="#ff5555"))
            else:
                self.kok.after(0, lambda: self.durum_etiketi.config(
                    text=f"✅  Sunucu: {SUNUCU_URL}", fg="#4caf50"))

                yeni_mesajlar = [m for m in mesajlar if m["id"] > son_mesaj_id]

                if yeni_mesajlar:
                    son_mesaj_id = mesajlar[-1]["id"]

                    def ui_guncelle():
                        # İlk açılışta tümünü yükle
                        if len(self.ic_cerceve.winfo_children()) == 0 and mesajlar:
                            for m in mesajlar:
                                self._kart_ekle(m["ad"], m["mesaj"], m["zaman"])
                        else:
                            for m in yeni_mesajlar:
                                self._kart_ekle(m["ad"], m["mesaj"], m["zaman"], yeni=True)

                        self.sayac_etiketi.config(
                            text=f"{len(mesajlar)} mesaj")
                        # En alta kaydır
                        self.kok.update_idletasks()
                        self.canvas.yview_moveto(1.0)

                    self.kok.after(0, ui_guncelle)

        threading.Thread(target=is_yap, daemon=True).start()
        self.kok.after(YENILEME_MS, self._guncelle)   # Bir sonraki güncellemeyi planla

# -----------------------------------------------------------
# BAŞLAT
# -----------------------------------------------------------

if __name__ == "__main__":
    kok = tk.Tk()
    uygulama = CanliDuvar(kok)
    print(f"[Canlı Duvar] Sunucu: {SUNUCU_URL}")
    print("[Canlı Duvar] Tam ekrandan çıkmak için: ESC")
    kok.mainloop()
