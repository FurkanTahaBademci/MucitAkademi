# ============================================================
#  HAFTA 24 - DERS 5: POST İSTEĞİ
# ============================================================
#
#  GET  = Sunucudan veri AL (okuma)
#  POST = Sunucuya veri GÖNDER (yazma/oluşturma)
#
#  POST ne zaman kullanılır?
#  - Yeni bir kullanıcı kaydetmek
#  - Yorum yazmak
#  - Form doldurup göndermek
#  - Ürün sepete eklemek
#
#  POST isteğinde veri "body" (gövde) kısmında gönderilir.
#  GET'te sorgu parametreleri URL'de görünürdü,
#  POST'ta gövdede olduğu için URL'de görünmez.
#
#  Durum kodları:
#  200 → OK (başarılı)
#  201 → Created (oluşturuldu) ← POST sonrası bunu görürüz
#  400 → Bad Request (yanlış istek)
#  401 → Unauthorized (yetkisiz)
#  403 → Forbidden (yasak)
#  404 → Not Found (bulunamadı)
#  500 → Server Error (sunucu hatası)
# ============================================================

import requests
import json

# -----------------------------------------------------------
# ÖRNEK 1: Yeni gönderi oluştur (POST)
# -----------------------------------------------------------
# Göndermek istediğimiz veri (Python sözlüğü)
yeni_gonderi = {
    "title": "Benim İlk API Gönderim",
    "body": "Bu gönderiyi Python ile API kullanarak oluşturdum!",
    "userId": 1
}

cevap = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=yeni_gonderi   # json= ile veriyi otomatik JSON formatında gönderir
)

print(f"Durum kodu: {cevap.status_code}")  # 201 = Created (oluşturuldu)
print()

# Sunucu oluşturduğu kaydı geri döner (ID ile birlikte)
olusturulan = cevap.json()
print("Sunucunun döndürdüğü veri:")
print(f"  ID    : {olusturulan['id']}")
print(f"  Başlık: {olusturulan['title']}")
print(f"  Body  : {olusturulan['body']}")

print()

# -----------------------------------------------------------
# ÖRNEK 2: Yeni yorum gönder
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 2: Yeni yorum yaz")
print("=" * 50)

yeni_yorum = {
    "postId": 1,
    "name": "Harika bir yazı!",
    "email": "ogrenci@example.com",
    "body": "Çok faydalı bilgiler, teşekkürler."
}

cevap = requests.post(
    "https://jsonplaceholder.typicode.com/comments",
    json=yeni_yorum
)

print(f"Durum kodu: {cevap.status_code}")
print(f"Oluşturulan yorum ID: {cevap.json()['id']}")

print()

# -----------------------------------------------------------
# ÖRNEK 3: GET vs POST farkını görelim
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 3: GET vs POST karşılaştırması")
print("=" * 50)

print("GET  isteği → Veri OKUR, sunucuyu değiştirmez")
print("POST isteği → Yeni veri YAZAR, sunucuyu değiştirir")
print()

# GET: Mevcut gönderileri oku
get_cevap = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"GET  durum kodu: {get_cevap.status_code}  (200 = OK)")

# POST: Yeni gönderi oluştur
post_cevap = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Test", "body": "Test içerik", "userId": 1}
)
print(f"POST durum kodu: {post_cevap.status_code}  (201 = Created)")

print()

# -----------------------------------------------------------
# ÖRNEK 4: Kullanıcıdan veri alarak gönderi oluştur
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 4: Kendi gönderini oluştur")
print("=" * 50)

baslik = input("Gönderi başlığı: ")
icerik = input("Gönderi içeriği: ")

gonderi = {
    "title": baslik,
    "body": icerik,
    "userId": 1
}

cevap = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=gonderi
)

if cevap.status_code == 201:
    sonuc = cevap.json()
    print()
    print("✓ Gönderi başarıyla oluşturuldu!")
    print(f"  Atanan ID: {sonuc['id']}")
    print(f"  Başlık   : {sonuc['title']}")
else:
    print(f"Hata! Durum kodu: {cevap.status_code}")

print()
print("Bir sonraki adım: 06_hata_yonetimi.py")
print("=" * 50)
