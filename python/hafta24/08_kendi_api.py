# ============================================================
#  HAFTA 24 - DERS 8: KENDİ API'Nİ YAZ (FLASK)
# ============================================================
#
#  Şimdiye kadar hep BAŞKASININ API'sini kullandık.
#  Şimdi KENDİ API'mizi yazacağız!
#
#  Flask = Python'un en popüler web framework'ü.
#  Birkaç satır kodla kendi sunucumuzu + API'mizi kurarız.
#
#  Önce Flask'ı yükle:
#       pip install flask
#
# ------------------------------------------------------------
#  Bu API'de neler olacak?
#
#  GET  /              → Karşılama mesajı
#  GET  /kullanicilar  → Tüm kullanıcıları listele
#  GET  /kullanicilar/1 → 1 numaralı kullanıcıyı getir
#  POST /kullanicilar  → Yeni kullanıcı ekle
#  GET  /hesapla?sayi1=5&sayi2=3 → İki sayıyı topla
#
# ------------------------------------------------------------
#  ÇALIŞTIRMAK İÇİN:
#
#  1. Bu dosyayı çalıştır: python 08_kendi_api.py
#  2. Tarayıcıya gir    : http://127.0.0.1:5000
#  3. Farklı endpoint'leri test et
#
#  Durdurmak için: Ctrl + C
# ============================================================

from flask import Flask, jsonify, request

# Flask uygulaması oluştur
uygulama = Flask(__name__)

# -----------------------------------------------------------
# Uygulamamızın "veritabanı" (şimdilik RAM'de tutuyoruz)
# -----------------------------------------------------------

kullanicilar = [
    {"id": 1, "ad": "Ahmet Yılmaz", "email": "ahmet@example.com", "yas": 28},
    {"id": 2, "ad": "Ayşe Kara",    "email": "ayse@example.com",  "yas": 24},
    {"id": 5, "ad": "Mehmet Demir", "email": "mehmet@example.com","yas": 32},
]

# -----------------------------------------------------------
# ENDPOINT 1: Ana sayfa
# GET /
# -----------------------------------------------------------

@uygulama.route("/")
def ana_sayfa():
    """API'ye hoş geldiniz mesajı"""
    return jsonify({
        "mesaj": "Benim API'me hoş geldiniz!- Furkan",
        "versiyon": "1.0",
        "endpoints": {
            "GET /kullanicilar": "Tüm kullanıcıları listele",
            "GET /kullanicilar/<id>": "Belirli kullanıcıyı getir",
            "POST /kullanicilar": "Yeni kullanıcı ekle",
            "GET /hesapla": "İki sayıyı topla (?sayi1=5&sayi2=3)"
        }
    })



@uygulama.route("/kullanicilar")
def kullanicilari_listele():
    """Tüm kullanıcıları döndürür"""
    return jsonify({
        "toplam": len(kullanicilar),
        "kullanicilar": kullanicilar
    })

# # -----------------------------------------------------------
# # ENDPOINT 3: Belirli kullanıcıyı getir
# # GET /kullanicilar/1
# # -----------------------------------------------------------

@uygulama.route("/kullanicilar/<int:kullanici_id>")
def kullanici_getir(kullanici_id):
    """ID'ye göre kullanıcı döndürür"""
    
    # Kullanıcıyı listede bul
    bulunan = None
    for k in kullanicilar:
        if k["id"] == kullanici_id:
            bulunan = k
            break
    
    if bulunan:
        return jsonify(bulunan)
    else:
        # 404 durum kodu ile hata mesajı gönder
        return jsonify({"hata": f"{kullanici_id} numaralı kullanıcı bulunamadı"}), 404

# # -----------------------------------------------------------
# # ENDPOINT 4: Yeni kullanıcı ekle
# # POST /kullanicilar
# # -----------------------------------------------------------

@uygulama.route("/kullanicilar", methods=["POST"])
def kullanici_ekle():
    """Yeni kullanıcı oluşturur"""
    
    # Gelen JSON verisini al
    veri = request.get_json()
    
    # Gerekli alanlar var mı kontrol et
    if not veri:
        return jsonify({"hata": "JSON verisi gönderilmedi"}), 400
    
    if "ad" not in veri or "email" not in veri:
        return jsonify({"hata": "'ad' ve 'email' alanları zorunludur"}), 400
    
    # Yeni kullanıcı oluştur
    yeni_id = max(k["id"] for k in kullanicilar) + 1
    yeni_kullanici = {
        "id": yeni_id,
        "ad": veri["ad"],
        "email": veri["email"],
        "yas": veri.get("yas", 0)  # yas yoksa 0 kullan
    }
    
    kullanicilar.append(yeni_kullanici)
    
    # 201 Created ile yeni kaydı döndür
    return jsonify({
        "mesaj": "Kullanıcı başarıyla oluşturuldu!",
        "kullanici": yeni_kullanici
    }), 201

# # -----------------------------------------------------------
# # ENDPOINT 5: Hesap makinesi
# # GET /hesapla?sayi1=5&sayi2=3
# # -----------------------------------------------------------

@uygulama.route("/hesapla")
def hesapla():
    """URL parametreriyle iki sayıyı toplar"""
    
    try:
        sayi1 = float(request.args.get("sayi1", 0))
        sayi2 = float(request.args.get("sayi2", 0))
    except ValueError:
        return jsonify({"hata": "Geçerli sayılar giriniz"}), 400
    
    return jsonify({
        "sayi1": sayi1,
        "sayi2": sayi2,
        "toplam": sayi1 + sayi2,
        "fark": sayi1 - sayi2,
        "carpim": sayi1 * sayi2,
        "bolum": sayi1 / sayi2 if sayi2 != 0 else "Sıfıra bölünemez"
    })

# # -----------------------------------------------------------
# # SUNUCUYU BAŞLAT
# # -----------------------------------------------------------

if __name__ == "__main__":
    import socket
    yerel_ip = socket.gethostbyname(socket.gethostname())

    print("=" * 50)
    print("  API SUNUCUSU BAŞLIYOR...")
    print("=" * 50)
    print()
    print("Aşağıdaki adresleri tarayıcında veya")
    print("başka bir Python dosyasından test edebilirsin:")
    print()
    print(f"  Yerel (bu bilgisayar) : http://127.0.0.1:5000/")
    print(f"  Yerel Ağ (diğer cihazlar): http://{yerel_ip}:5000/")
    print()
    print(f"  http://{yerel_ip}:5000/kullanicilar")
    print(f"  http://{yerel_ip}:5000/kullanicilar/1")
    print(f"  http://{yerel_ip}:5000/hesapla?sayi1=10&sayi2=4")
    print()
    print("Durdurmak için: Ctrl + C")
    print("=" * 50)

    # host="0.0.0.0" → Yerel ağdaki tüm cihazlar erişebilir
    # debug=True → Kod değişince otomatik yeniden yükle
    uygulama.run(host="0.0.0.0", port=5000, debug=True)
