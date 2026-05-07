# ============================================================
#  HAFTA 24 - DERS 2: İLK GET İSTEĞİ
# ============================================================
#
#  Önce "requests" kütüphanesini yüklememiz gerekiyor.
#  Terminal'e şunu yaz:
#
#       pip install requests
#
# ------------------------------------------------------------
#  Biz bu derste JSONPlaceholder kullanacağız.
#  JSONPlaceholder = Ücretsiz, sahte (fake) bir REST API.
#  Test ve öğrenme amaçlı yapılmış. Gerçek veri gibi davranır.
#
#  Adres: https://jsonplaceholder.typicode.com
#
# ------------------------------------------------------------
#  GET isteği = "Bana şu adresten veri AL"
#
#  Tarayıcıya bir adres yazmak da aslında GET isteğidir!
# ============================================================

import requests 

# requests.get() → bir adrese GET isteği gönderir
# Sanki tarayıcıya o adresi yazmak gibi, ama Python ile!
cevap = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Durum kodu nedir?
# 200 = Her şey yolunda (OK)
# 404 = Bulunamadı
# 500 = Sunucu hatası
print(f"Durum kodu: {cevap.status_code}")

kullanici = cevap.json()

print(f"Ad   : {kullanici['name']}")
print(f"Email: {kullanici['email']}")
print(f"Şehir: {kullanici['address']['city']}")
print(f"Enlem: {kullanici['address']['geo']['lat']}")
print(f"Boylam: {kullanici['address']['geo']['lng']}")

# print()

# # -----------------------------------------------------------
# # ÖRNEK 2: Tüm kullanıcıları al
# # -----------------------------------------------------------

# print("=" * 50)
# print("ÖRNEK 2: Tüm kullanıcılar")
# print("=" * 50)

cevap = requests.get("https://jsonplaceholder.typicode.com/users")

# Bu sefer liste gelecek, çünkü birden fazla kullanıcı var
kullanicilar = cevap.json()

print(f"Toplam kullanıcı sayısı: {len(kullanicilar)}")
print()
print("İsimler:")

for kullanici in kullanicilar:
    print(f"  - {kullanici['name']}  ({kullanici['email']})")

# print()

# # -----------------------------------------------------------
# # ÖRNEK 3: Gönderi (post) al
# # -----------------------------------------------------------

# print("=" * 50)
print("ÖRNEK 3: İlk gönderiyi al")
print("=" * 50)

cevap = requests.get("https://jsonplaceholder.typicode.com/posts/1")
gonderi = cevap.json()

print(f"Başlık: {gonderi['title']}")
print(f"İçerik: {gonderi['body'][:80]}...")  # İlk 80 karakteri göster

# print()
# print("Bir sonraki adım: 03_json_anlama.py")
# print("=" * 50)
