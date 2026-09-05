# ============================================================
#  LAN SOHBET UYGULAMASI - GÖRSEL ARAYÜZ (GUI)
# ============================================================
#
#  Tkinter ile yapılmış görsel sohbet uygulaması.
#  Kurulum gerekmez, Python ile birlikte gelir!
#
#  ÇALIŞTIRMAK:
#    python istemci_gui.py
#
#  Açılan pencerede:
#    1. Sunucu IP'sini gir
#    2. Port numarasını gir (varsayılan 5555)
#    3. Kullanıcı adını gir
#    4. "Bağlan" butonuna tıkla
#    5. Mesaj yaz, Enter veya "Gönder" butonuna bas
#
# ============================================================

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, font

# -----------------------------------------------------------
# RENK AYARLARI (kolay değiştirilebilir tema)
# -----------------------------------------------------------

TEMA = {
    "arka_plan"     : "#1e1e2e",   # Koyu mavi-mor arka plan
    "panel_bg"      : "#2a2a3d",   # Biraz daha açık panel
    "mesaj_bg"      : "#13131f",   # Mesaj alanı (çok koyu)
    "mesaj_fg"      : "#cdd6f4",   # Mesaj yazı rengi (açık)
    "giris_bg"      : "#2a2a3d",   # Giriş kutusu arka planı
    "giris_fg"      : "#cdd6f4",   # Giriş kutusu yazı rengi
    "buton_bg"      : "#89b4fa",   # Buton arka planı (mavi)
    "buton_fg"      : "#1e1e2e",   # Buton yazı rengi
    "etiket_fg"     : "#a6adc8",   # Etiket yazı rengi
    "baslik_fg"     : "#cba6f7",   # Başlık rengi (mor)
    "sistem_renk"   : "#a6e3a1",   # Sistem mesajları (yeşil)
    "kendi_renk"    : "#89dceb",   # Kendi mesajlarımız (açık mavi)
    "diger_renk"    : "#cdd6f4",   # Diğerlerinin mesajları
}

# -----------------------------------------------------------
# ANA UYGULAMA SINIFI
# -----------------------------------------------------------

class SohbetUygulamasi:

    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("LAN Sohbet")
        self.pencere.configure(bg=TEMA["arka_plan"])
        self.pencere.resizable(True, True)
        self.pencere.minsize(500, 400)

        self.sunucu_socket = None
        self.bagli        = False
        self.nickname     = ""

        self._arayuz_olustur()
        self.pencere.protocol("WM_DELETE_WINDOW", self._kapat)

    # -------------------------------------------------------
    # ARAYÜZ OLUŞTURMA
    # -------------------------------------------------------

    def _arayuz_olustur(self):
        """Tüm tkinter widget'larını oluşturur"""

        # --- Başlık ---
        baslik_frame = tk.Frame(self.pencere, bg=TEMA["arka_plan"], pady=8)
        baslik_frame.pack(fill=tk.X)

        tk.Label(
            baslik_frame,
            text="💬  LAN Sohbet",
            font=("Helvetica", 16, "bold"),
            bg=TEMA["arka_plan"],
            fg=TEMA["baslik_fg"]
        ).pack()

        # --- Bağlantı Paneli ---
        baglanti_frame = tk.Frame(self.pencere, bg=TEMA["panel_bg"], padx=10, pady=8)
        baglanti_frame.pack(fill=tk.X, padx=10, pady=(0, 8))

        # IP
        tk.Label(baglanti_frame, text="Sunucu IP:", bg=TEMA["panel_bg"], fg=TEMA["etiket_fg"]).grid(
            row=0, column=0, sticky="e", padx=(0, 4), pady=3)
        self.ip_entry = tk.Entry(
            baglanti_frame, width=15,
            bg=TEMA["giris_bg"], fg=TEMA["giris_fg"],
            insertbackground=TEMA["giris_fg"], relief="flat", bd=4
        )
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.grid(row=0, column=1, padx=4, pady=3)

        # Port
        tk.Label(baglanti_frame, text="Port:", bg=TEMA["panel_bg"], fg=TEMA["etiket_fg"]).grid(
            row=0, column=2, sticky="e", padx=(8, 4), pady=3)
        self.port_entry = tk.Entry(
            baglanti_frame, width=6,
            bg=TEMA["giris_bg"], fg=TEMA["giris_fg"],
            insertbackground=TEMA["giris_fg"], relief="flat", bd=4
        )
        self.port_entry.insert(0, "5555")
        self.port_entry.grid(row=0, column=3, padx=4, pady=3)

        # Kullanıcı Adı
        tk.Label(baglanti_frame, text="Adın:", bg=TEMA["panel_bg"], fg=TEMA["etiket_fg"]).grid(
            row=0, column=4, sticky="e", padx=(8, 4), pady=3)
        self.nick_entry = tk.Entry(
            baglanti_frame, width=12,
            bg=TEMA["giris_bg"], fg=TEMA["giris_fg"],
            insertbackground=TEMA["giris_fg"], relief="flat", bd=4
        )
        self.nick_entry.grid(row=0, column=5, padx=4, pady=3)
        self.nick_entry.bind("<Return>", lambda e: self._baglan())

        # Bağlan Butonu
        self.baglanti_btn = tk.Button(
            baglanti_frame,
            text="Bağlan",
            bg=TEMA["buton_bg"], fg=TEMA["buton_fg"],
            font=("Helvetica", 9, "bold"),
            relief="flat", bd=0, padx=10, cursor="hand2",
            command=self._baglan
        )
        self.baglanti_btn.grid(row=0, column=6, padx=(8, 0), pady=3)

        # Durum etiketi
        self.durum_etiket = tk.Label(
            baglanti_frame,
            text="● Bağlantı yok",
            bg=TEMA["panel_bg"], fg="#f38ba8",   # Kırmızı = bağlı değil
            font=("Helvetica", 8)
        )
        self.durum_etiket.grid(row=1, column=0, columnspan=7, sticky="w", pady=(2, 0))

        # --- Mesaj Alanı ---
        mesaj_frame = tk.Frame(self.pencere, bg=TEMA["arka_plan"])
        mesaj_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 6))

        self.mesaj_alani = scrolledtext.ScrolledText(
            mesaj_frame,
            state="disabled",
            bg=TEMA["mesaj_bg"],
            fg=TEMA["mesaj_fg"],
            font=("Consolas", 10),
            relief="flat", bd=6,
            wrap=tk.WORD,
            insertbackground=TEMA["mesaj_fg"]
        )
        self.mesaj_alani.pack(fill=tk.BOTH, expand=True)

        # Renk etiketleri (farklı mesaj türleri için)
        self.mesaj_alani.tag_config("sistem",  foreground=TEMA["sistem_renk"], font=("Consolas", 10, "italic"))
        self.mesaj_alani.tag_config("kendi",   foreground=TEMA["kendi_renk"])
        self.mesaj_alani.tag_config("diger",   foreground=TEMA["diger_renk"])

        # --- Gönderme Alanı ---
        alt_frame = tk.Frame(self.pencere, bg=TEMA["panel_bg"], padx=10, pady=8)
        alt_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        alt_frame.columnconfigure(0, weight=1)

        self.mesaj_entry = tk.Entry(
            alt_frame,
            bg=TEMA["giris_bg"], fg=TEMA["giris_fg"],
            insertbackground=TEMA["giris_fg"],
            font=("Consolas", 11),
            relief="flat", bd=4,
            state="disabled"
        )
        self.mesaj_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8), ipady=4)
        self.mesaj_entry.bind("<Return>", lambda e: self._mesaj_gonder())

        self.gonder_btn = tk.Button(
            alt_frame,
            text="Gönder  ▶",
            bg=TEMA["buton_bg"], fg=TEMA["buton_fg"],
            font=("Helvetica", 10, "bold"),
            relief="flat", bd=0, padx=12, pady=4,
            cursor="hand2",
            state="disabled",
            command=self._mesaj_gonder
        )
        self.gonder_btn.grid(row=0, column=1)

    # -------------------------------------------------------
    # BAĞLANTI KURMA
    # -------------------------------------------------------

    def _baglan(self):
        """Sunucuya bağlanır"""

        ip       = self.ip_entry.get().strip()
        port_str = self.port_entry.get().strip()
        nick     = self.nick_entry.get().strip()

        # Doğrulama
        if not ip:
            messagebox.showerror("Hata", "Sunucu IP adresi boş olamaz!")
            return
        if not port_str.isdigit():
            messagebox.showerror("Hata", "Port numarası geçersiz!")
            return
        if not nick:
            messagebox.showerror("Hata", "Kullanıcı adı boş olamaz!")
            return

        port = int(port_str)
        self.nickname = nick

        self._sistem_mesaji(f"[*] {ip}:{port} adresine bağlanılıyor...")

        # Arka planda bağlan (UI'ın donmaması için)
        t = threading.Thread(target=self._baglan_thread, args=(ip, port, nick), daemon=True)
        t.start()

    def _baglan_thread(self, ip, port, nick):
        """Bağlantıyı ayrı thread'de kurar"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)   # 5 saniye içinde bağlanamazsa hata ver
            s.connect((ip, port))
            s.settimeout(None)  # Bağlandıktan sonra timeout kaldır

            # Protokol: sunucu "NICK?" gönderir, biz nickname'i göndeririz
            istek = s.recv(1024).decode("utf-8")
            if istek != "NICK?":
                raise Exception("Geçersiz sunucu protokolü")

            s.send(nick.encode("utf-8"))

            self.sunucu_socket = s
            self.bagli = True

            # UI güncellemelerini ana thread'e bırak
            self.pencere.after(0, self._baglanti_basarili)

            # Mesaj dinleme döngüsünü başlat
            self._mesaj_dinle()

        except ConnectionRefusedError:
            self.pencere.after(0, lambda: messagebox.showerror(
                "Bağlantı Hatası",
                f"Bağlantı reddedildi!\n\n"
                f"• {ip}:{port} adresinde sunucu çalışıyor mu?\n"
                f"• IP adresi ve port doğru mu?"
            ))
            self.pencere.after(0, lambda: self._sistem_mesaji("[X] Bağlantı başarısız."))

        except OSError as e:
            self.pencere.after(0, lambda: messagebox.showerror("Bağlantı Hatası", str(e)))
            self.pencere.after(0, lambda: self._sistem_mesaji(f"[X] Hata: {e}"))

    def _baglanti_basarili(self):
        """Bağlantı başarılı olunca UI'ı günceller"""
        self.baglanti_btn.config(text="Bağlı ✓", state="disabled", bg="#a6e3a1")
        self.mesaj_entry.config(state="normal")
        self.gonder_btn.config(state="normal")
        self.durum_etiket.config(text=f"● Bağlı  ({self.nickname})", fg="#a6e3a1")
        self.mesaj_entry.focus()
        self._sistem_mesaji(f"[✓] Bağlandın! Hoş geldin, {self.nickname}!")
        self._sistem_mesaji("    Mesaj yaz ve Enter'a bas.\n")

    # -------------------------------------------------------
    # MESAJ DINLEME (ayrı thread)
    # -------------------------------------------------------

    def _mesaj_dinle(self):
        """Sunucudan gelen mesajları alır ve ekranda gösterir"""
        while self.bagli:
            try:
                veri = self.sunucu_socket.recv(2048)
                if not veri:
                    break

                mesaj = veri.decode("utf-8")

                # Ana thread'den UI güncelle (thread güvenliği)
                self.pencere.after(0, lambda m=mesaj: self._mesaj_goster(m))

            except Exception:
                break

        # Döngü bitti = bağlantı koptu
        self.pencere.after(0, self._baglanti_kesildi)

    # -------------------------------------------------------
    # MESAJ GÖNDERME
    # -------------------------------------------------------

    def _mesaj_gonder(self):
        """Giriş kutusundaki mesajı sunucuya gönderir"""
        if not self.bagli:
            messagebox.showwarning("Uyarı", "Önce sunucuya bağlanmalısın!")
            return

        mesaj = self.mesaj_entry.get().strip()
        if not mesaj:
            return

        try:
            self.sunucu_socket.send(mesaj.encode("utf-8"))
            self.mesaj_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Gönderim Hatası", str(e))

    # -------------------------------------------------------
    # MESAJ GÖSTERİM
    # -------------------------------------------------------

    def _mesaj_goster(self, mesaj):
        """Gelen mesajı uygun renkte mesaj alanına ekler"""
        self.mesaj_alani.config(state="normal")

        # Mesaj türüne göre renk belirle
        if "***" in mesaj:
            etiket = "sistem"     # Katılma/ayrılma bildirimleri
        elif mesaj.startswith(f"[{self.nickname}]:"):
            etiket = "kendi"      # Kendi mesajımız
        else:
            etiket = "diger"      # Başkasının mesajı

        self.mesaj_alani.insert(tk.END, mesaj, etiket)

        # Her zaman en alta kaydır
        self.mesaj_alani.see(tk.END)
        self.mesaj_alani.config(state="disabled")

    def _sistem_mesaji(self, metin):
        """Sistem mesajı (gri/italik) gösterir"""
        self.mesaj_alani.config(state="normal")
        self.mesaj_alani.insert(tk.END, metin + "\n", "sistem")
        self.mesaj_alani.see(tk.END)
        self.mesaj_alani.config(state="disabled")

    # -------------------------------------------------------
    # BAĞLANTI KESİLDİ / KAPAT
    # -------------------------------------------------------

    def _baglanti_kesildi(self):
        """Bağlantı kesilince UI'ı sıfırlar"""
        self.bagli = False
        self.durum_etiket.config(text="● Bağlantı kesildi", fg="#f38ba8")
        self._sistem_mesaji("\n[!] Sunucu bağlantısı kesildi.")
        self.mesaj_entry.config(state="disabled")
        self.gonder_btn.config(state="disabled")
        self.baglanti_btn.config(text="Yeniden Bağlan", state="normal", bg=TEMA["buton_bg"])

    def _kapat(self):
        """Pencere kapatılırken bağlantıyı düzgün sonlandırır"""
        if self.sunucu_socket:
            try:
                self.sunucu_socket.close()
            except Exception:
                pass
        self.pencere.destroy()

# -----------------------------------------------------------
# UYGULAMA BAŞLAT
# -----------------------------------------------------------

if __name__ == "__main__":
    pencere = tk.Tk()

    # Pencere ayarları
    pencere.geometry("680x520")

    uygulama = SohbetUygulamasi(pencere)

    pencere.mainloop()
