# ============================================================
#  HAFTA 25 - CANLI ANONİM DUVAR: ÖĞRENCİ İSTEMCİSİ (GUI)
# ============================================================
#
#  Bu dosya ÖĞRENCİLERİN bilgisayarında çalışır.
#  Mesaj göndermek için grafiksel bir arayüz sunar.
#
#  ÇALIŞTIRMAK:
#    python istemci_gui.py
#
#  Sunucu IP'sini giriş ekranında değiştirebilirsin.
#  (Öğretmen sunucu.py'yi başlatınca IP'yi söyler)
#
# ============================================================

import tkinter as tk
from tkinter import messagebox
import urllib.request
import urllib.error
import json
import threading

# -----------------------------------------------------------
# AYARLAR
# -----------------------------------------------------------

VARSAYILAN_IP = "127.0.0.1"   # Öğrenciler kendi ağ IP'lerini girecek
PORT = 5000

# Renkler
ARKAPLAN  = "#1a1a2e"
PANEL     = "#16213e"
VURGU     = "#e94560"
METIN     = "#eeeeee"
GRI_METIN = "#888888"
GIRIS_BG  = "#0f3460"

# -----------------------------------------------------------
# YARDIMCI: POST isteği gönder
# -----------------------------------------------------------

def mesaj_gonder(sunucu_url, ad, mesaj):
    """
    Sunucuya POST isteği gönderir.
    Döndürür: (basari: bool, mesaj: str)
    """
    veri = json.dumps({"ad": ad, "mesaj": mesaj}).encode("utf-8")
    istek = urllib.request.Request(
        url=f"{sunucu_url}/mesaj",
        data=veri,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(istek, timeout=5) as yanit:
            return True, "Mesajın duvara eklendi! 🎉"
    except urllib.error.HTTPError as e:
        try:
            hata_veri = json.loads(e.read().decode())
            return False, hata_veri.get("hata", f"HTTP Hatası: {e.code}")
        except Exception:
            return False, f"HTTP Hatası: {e.code}"
    except urllib.error.URLError:
        return False, "Sunucuya bağlanılamadı. IP adresini kontrol et!"
    except Exception as e:
        return False, str(e)

# -----------------------------------------------------------
# TKINTER ARAYÜZÜ
# -----------------------------------------------------------

class IstemciGUI:
    def __init__(self, kok):
        self.kok = kok
        self.kok.title("📌 Anonim Duvar - Mesaj Gönder")
        self.kok.configure(bg=ARKAPLAN)
        self.kok.resizable(False, False)

        self.sunucu_url = f"http://{VARSAYILAN_IP}:{PORT}"

        self._arayuz_kur()
        self._pencere_ortala(480, 520)

    # -------------------------------------------------------
    def _pencere_ortala(self, en, boy):
        self.kok.update_idletasks()
        ekran_en  = self.kok.winfo_screenwidth()
        ekran_boy = self.kok.winfo_screenheight()
        x = (ekran_en  - en)  // 2
        y = (ekran_boy - boy) // 2
        self.kok.geometry(f"{en}x{boy}+{x}+{y}")

    # -------------------------------------------------------
    def _arayuz_kur(self):
        # Başlık
        tk.Label(
            self.kok, text="📌 Canlı Anonim Duvar",
            font=("Segoe UI", 20, "bold"),
            bg=ARKAPLAN, fg=VURGU
        ).pack(pady=(25, 4))

        tk.Label(
            self.kok, text="Adını veya takma adını yaz, mesajını bırak!",
            font=("Segoe UI", 11),
            bg=ARKAPLAN, fg=GRI_METIN
        ).pack(pady=(0, 20))

        # Sunucu IP satırı
        ip_cerceve = tk.Frame(self.kok, bg=ARKAPLAN)
        ip_cerceve.pack(fill="x", padx=40)

        tk.Label(
            ip_cerceve, text="Sunucu IP:",
            font=("Segoe UI", 10), bg=ARKAPLAN, fg=GRI_METIN
        ).pack(side="left")

        self.ip_girdi = tk.Entry(
            ip_cerceve,
            font=("Segoe UI", 10),
            bg=GIRIS_BG, fg=METIN,
            insertbackground=METIN,
            relief="flat", bd=4,
            width=20
        )
        self.ip_girdi.insert(0, VARSAYILAN_IP)
        self.ip_girdi.pack(side="left", padx=(8, 0))

        tk.Button(
            ip_cerceve, text="Bağlan",
            font=("Segoe UI", 9, "bold"),
            bg=VURGU, fg="white",
            relief="flat", cursor="hand2",
            command=self._baglan
        ).pack(side="left", padx=(8, 0))

        self.baglanti_etiketi = tk.Label(
            self.kok, text="",
            font=("Segoe UI", 9),
            bg=ARKAPLAN, fg=GRI_METIN
        )
        self.baglanti_etiketi.pack(pady=(4, 0))

        # Ana form
        form = tk.Frame(self.kok, bg=PANEL, bd=0)
        form.pack(fill="x", padx=40, pady=16)

        # Ad alanı
        tk.Label(
            form, text="👤  Adın veya takma adın",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL, fg=METIN, anchor="w"
        ).pack(fill="x", padx=20, pady=(18, 4))

        self.ad_girdi = tk.Entry(
            form,
            font=("Segoe UI", 12),
            bg=GIRIS_BG, fg=METIN,
            insertbackground=METIN,
            relief="flat", bd=6
        )
        self.ad_girdi.insert(0, "Anonim")
        self.ad_girdi.pack(fill="x", padx=20, pady=(0, 12))

        # Mesaj alanı
        tk.Label(
            form, text="💬  Mesajın",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL, fg=METIN, anchor="w"
        ).pack(fill="x", padx=20)

        self.mesaj_girdi = tk.Text(
            form,
            font=("Segoe UI", 12),
            bg=GIRIS_BG, fg=METIN,
            insertbackground=METIN,
            relief="flat", bd=6,
            height=5, wrap="word"
        )
        self.mesaj_girdi.pack(fill="x", padx=20, pady=(4, 4))

        # Karakter sayacı
        self.karakter_etiketi = tk.Label(
            form, text="0 / 300",
            font=("Segoe UI", 9),
            bg=PANEL, fg=GRI_METIN, anchor="e"
        )
        self.karakter_etiketi.pack(fill="x", padx=20, pady=(0, 14))
        self.mesaj_girdi.bind("<KeyRelease>", self._karakter_say)

        # Gönder butonu
        self.gonder_buton = tk.Button(
            self.kok, text="🚀  Gönder",
            font=("Segoe UI", 13, "bold"),
            bg=VURGU, fg="white",
            activebackground="#c73652",
            relief="flat", cursor="hand2",
            pady=10,
            command=self._gonder
        )
        self.gonder_buton.pack(fill="x", padx=40, pady=(0, 10))

        # Durum mesajı
        self.durum_etiketi = tk.Label(
            self.kok, text="",
            font=("Segoe UI", 11),
            bg=ARKAPLAN, fg=GRI_METIN
        )
        self.durum_etiketi.pack(pady=(0, 15))

        # Enter ile gönderme (Ctrl+Enter)
        self.kok.bind("<Control-Return>", lambda e: self._gonder())

    # -------------------------------------------------------
    def _karakter_say(self, event=None):
        sayi = len(self.mesaj_girdi.get("1.0", "end-1c"))
        renk = "#e94560" if sayi > 300 else GRI_METIN
        self.karakter_etiketi.config(text=f"{sayi} / 300", fg=renk)

    # -------------------------------------------------------
    def _baglan(self):
        ip = self.ip_girdi.get().strip()
        if not ip:
            return
        self.sunucu_url = f"http://{ip}:{PORT}"
        self.baglanti_etiketi.config(text=f"Sunucu: {self.sunucu_url}", fg=GRI_METIN)

        # Bağlantıyı test et
        def test():
            try:
                with urllib.request.urlopen(self.sunucu_url + "/mesajlar", timeout=3):
                    self.kok.after(0, lambda: self.baglanti_etiketi.config(
                        text=f"✅  Bağlandı: {self.sunucu_url}", fg="#4caf50"))
            except Exception:
                self.kok.after(0, lambda: self.baglanti_etiketi.config(
                    text=f"❌  Bağlanamadı: {self.sunucu_url}", fg="#e94560"))

        threading.Thread(target=test, daemon=True).start()

    # -------------------------------------------------------
    def _gonder(self):
        ad    = self.ad_girdi.get().strip() or "Anonim"
        mesaj = self.mesaj_girdi.get("1.0", "end-1c").strip()

        if not mesaj:
            self._durum_goster("⚠️  Mesaj boş olamaz!", "#ff9800")
            return
        if len(mesaj) > 300:
            self._durum_goster("⚠️  Mesaj 300 karakterden uzun!", "#ff9800")
            return

        self.gonder_buton.config(state="disabled", text="Gönderiliyor...")

        def is_yap():
            basari, bilgi = mesaj_gonder(self.sunucu_url, ad, mesaj)
            def ui():
                self.gonder_buton.config(state="normal", text="🚀  Gönder")
                if basari:
                    self.mesaj_girdi.delete("1.0", "end")
                    self.karakter_etiketi.config(text="0 / 300", fg=GRI_METIN)
                    self._durum_goster(bilgi, "#4caf50")
                else:
                    self._durum_goster(f"❌  {bilgi}", "#e94560")
            self.kok.after(0, ui)

        threading.Thread(target=is_yap, daemon=True).start()

    # -------------------------------------------------------
    def _durum_goster(self, metin, renk):
        self.durum_etiketi.config(text=metin, fg=renk)
        self.kok.after(4000, lambda: self.durum_etiketi.config(text=""))

# -----------------------------------------------------------
# BAŞLAT
# -----------------------------------------------------------

if __name__ == "__main__":
    kok = tk.Tk()
    uygulama = IstemciGUI(kok)
    kok.mainloop()
