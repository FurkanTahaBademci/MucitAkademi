# ============================================================
#  HAFTA 25 - CANLI ANONİM DUVAR: SUNUCU
# ============================================================
#
#  Bu dosya SADECE senin bilgisayarında çalışır (öğretmen).
#  Sınıftaki herkes aynı Wi-Fi / LAN üzerindeyse mesaj gönderebilir.
#
#  KURULUM (bir kez):
#    pip install flask flask-cors
#
#  ÇALIŞTIRMAK:
#    python sunucu.py
#
#  Sunucu başlayınca ekrana IP adresini yazar.
#  Öğrenciler o IP'yi istemci_gui.py'ye yazarlar.
#
# ------------------------------------------------------------
#  ENDPOINT'LER:
#
#  GET  /            → Ana sayfa (bilgi)
#  GET  /mesajlar    → Tüm mesajları JSON olarak getir
#  POST /mesaj       → Yeni mesaj gönder  { "ad": "...", "mesaj": "..." }
#  DELETE /temizle   → Tüm mesajları sil (sadece yönetici)
#
# ============================================================

import socket
import threading
from datetime import datetime
from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

# -----------------------------------------------------------
# AYARLAR
# -----------------------------------------------------------

PORT        = 5000          # Sunucunun dinleyeceği port
YONETİCİ_SIFRE = "mucit25"  # DELETE /temizle için şifre

# -----------------------------------------------------------
# FLASK UYGULAMASI
# -----------------------------------------------------------

uygulama = Flask(__name__)
CORS(uygulama)   # Tarayıcıdan çapraz-origin isteğine izin ver

# Mesajlar bellekte tutulur (sunucu kapanınca sıfırlanır)
mesajlar = []
mesaj_sayaci = 0
kilit = threading.Lock()

# -----------------------------------------------------------
# YARDIMCI: Yerel IP bul
# -----------------------------------------------------------

def yerel_ip_bul():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# -----------------------------------------------------------
# HTML ŞABLONU (tarayıcıdan mesaj göndermek için)
# -----------------------------------------------------------

HTML_SAYFASI = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anonim Duvar 📌</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #1a1a2e;
            color: #eee;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px 15px;
        }
        h1 { font-size: 2rem; margin-bottom: 8px; color: #e94560; }
        p.alt { color: #aaa; margin-bottom: 25px; font-size: 0.9rem; }
        .form-kutu {
            background: #16213e;
            border-radius: 12px;
            padding: 24px;
            width: 100%;
            max-width: 480px;
            margin-bottom: 30px;
        }
        input, textarea {
            width: 100%;
            padding: 10px 14px;
            border-radius: 8px;
            border: 1px solid #333;
            background: #0f3460;
            color: #fff;
            font-size: 1rem;
            margin-bottom: 12px;
        }
        textarea { resize: vertical; min-height: 80px; }
        button {
            width: 100%;
            padding: 12px;
            background: #e94560;
            color: #fff;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover { background: #c73652; }
        #durum { margin-top: 10px; text-align: center; font-size: 0.9rem; }
        .mesaj-listesi { width: 100%; max-width: 480px; }
        .mesaj-karti {
            background: #16213e;
            border-left: 4px solid #e94560;
            border-radius: 8px;
            padding: 14px 18px;
            margin-bottom: 14px;
            animation: gir 0.3s ease;
        }
        @keyframes gir { from { opacity:0; transform:translateY(-8px); } to { opacity:1; } }
        .mesaj-ad { font-weight: bold; color: #e94560; margin-bottom: 6px; }
        .mesaj-icerik { font-size: 1rem; line-height: 1.4; }
        .mesaj-zaman { font-size: 0.75rem; color: #888; margin-top: 6px; }
    </style>
</head>
<body>
    <h1>📌 Anonim Duvar</h1>
    <p class="alt">Adını (veya takma adını) yaz, mesajını bırak!</p>

    <div class="form-kutu">
        <input id="ad" type="text" placeholder="Adın veya takma adın (örn: Anonim, Uzay Korsanı...)" maxlength="30">
        <textarea id="mesaj" placeholder="Mesajını yaz... 💬" maxlength="300"></textarea>
        <button onclick="gonder()">Gönder 🚀</button>
        <div id="durum"></div>
    </div>

    <div class="mesaj-listesi" id="mesajlar"></div>

    <script>
        async function gonder() {
            const ad = document.getElementById('ad').value.trim() || 'Anonim';
            const mesaj = document.getElementById('mesaj').value.trim();
            if (!mesaj) { durum('⚠️ Mesaj boş olamaz!', 'orange'); return; }

            const yanit = await fetch('/mesaj', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ ad, mesaj })
            });
            if (yanit.ok) {
                document.getElementById('mesaj').value = '';
                durum('✅ Mesajın gönderildi!', '#4caf50');
                yukle();
            } else {
                durum('❌ Bir hata oluştu.', '#e94560');
            }
        }

        function durum(metin, renk) {
            const el = document.getElementById('durum');
            el.textContent = metin;
            el.style.color = renk;
            setTimeout(() => el.textContent = '', 3000);
        }

        async function yukle() {
            const yanit = await fetch('/mesajlar');
            const veri  = await yanit.json();
            const liste = document.getElementById('mesajlar');
            liste.innerHTML = '';
            veri.mesajlar.slice().reverse().forEach(m => {
                liste.innerHTML += `
                <div class="mesaj-karti">
                    <div class="mesaj-ad">👤 ${m.ad}</div>
                    <div class="mesaj-icerik">${m.mesaj}</div>
                    <div class="mesaj-zaman">${m.zaman}</div>
                </div>`;
            });
        }

        // Her 3 saniyede mesajları yenile
        yukle();
        setInterval(yukle, 3000);
    </script>
</body>
</html>
"""

# -----------------------------------------------------------
# ENDPOINT 1: Ana sayfa (tarayıcıdan mesaj gönderme arayüzü)
# GET /
# -----------------------------------------------------------

@uygulama.route("/")
def ana_sayfa():
    return render_template_string(HTML_SAYFASI)

# -----------------------------------------------------------
# ENDPOINT 2: Tüm mesajları getir
# GET /mesajlar
# -----------------------------------------------------------

@uygulama.route("/mesajlar", methods=["GET"])
def mesajlari_getir():
    with kilit:
        return jsonify({
            "toplam": len(mesajlar),
            "mesajlar": mesajlar
        })

# -----------------------------------------------------------
# ENDPOINT 3: Yeni mesaj gönder
# POST /mesaj
# Body: { "ad": "...", "mesaj": "..." }
# -----------------------------------------------------------

@uygulama.route("/mesaj", methods=["POST"])
def mesaj_ekle():
    global mesaj_sayaci

    veri = request.get_json()
    if not veri or "mesaj" not in veri:
        return jsonify({"hata": "'mesaj' alanı zorunludur."}), 400

    icerik = str(veri.get("mesaj", "")).strip()
    ad     = str(veri.get("ad", "Anonim")).strip() or "Anonim"

    if len(icerik) == 0:
        return jsonify({"hata": "Mesaj boş olamaz."}), 400
    if len(icerik) > 300:
        return jsonify({"hata": "Mesaj en fazla 300 karakter olabilir."}), 400
    if len(ad) > 30:
        return jsonify({"hata": "Ad en fazla 30 karakter olabilir."}), 400

    with kilit:
        mesaj_sayaci += 1
        yeni = {
            "id"   : mesaj_sayaci,
            "ad"   : ad,
            "mesaj": icerik,
            "zaman": datetime.now().strftime("%H:%M:%S")
        }
        mesajlar.append(yeni)

    print(f"[YENİ MESAJ] {ad}: {icerik}")
    return jsonify({"basari": True, "mesaj": yeni}), 201

# -----------------------------------------------------------
# ENDPOINT 4: Tüm mesajları temizle (yönetici)
# DELETE /temizle
# Header: X-Sifre: mucit25
# -----------------------------------------------------------

@uygulama.route("/temizle", methods=["DELETE"])
def temizle():
    sifre = request.headers.get("X-Sifre", "")
    if sifre != YONETİCİ_SIFRE:
        return jsonify({"hata": "Yetkisiz erişim."}), 403

    with kilit:
        mesajlar.clear()
    print("[TEMİZLENDİ] Tüm mesajlar silindi.")
    return jsonify({"basari": True, "mesaj": "Tüm mesajlar silindi."})

# -----------------------------------------------------------
# BAŞLAT
# -----------------------------------------------------------

if __name__ == "__main__":
    ip = yerel_ip_bul()
    print("=" * 55)
    print("  📌 ANONİM DUVAR SUNUCUSU BAŞLADI")
    print("=" * 55)
    print(f"  Yerel erişim  : http://127.0.0.1:{PORT}")
    print(f"  Sınıf erişimi : http://{ip}:{PORT}")
    print(f"  Mesajları izle: http://{ip}:{PORT}/mesajlar")
    print("=" * 55)
    print("  Durdurmak için: Ctrl + C")
    print()
    uygulama.run(host="0.0.0.0", port=PORT, debug=False)
