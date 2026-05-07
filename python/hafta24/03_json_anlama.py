# ============================================================
#  HAFTA 24 - DERS 3: JSON VERİYİ ANLAMA
# ============================================================
#
#  JSON = JavaScript Object Notation
#       (Veri taşıma formatı)
#
#  API'lerden gelen veriler genellikle JSON formatındadır.
#  JSON, Python'daki sözlük (dict) ve liste (list) yapısına
#  çok benzer!
#
#  JSON ÖRNEK:
#  {
#    "isim": "Ali",
#    "yas": 25,
#    "hobiler": ["futbol", "müzik"],
#    "adres": {
#      "şehir": "İstanbul",
#      "ilce": "Kadıköy"
#    }
#  }
#
#  Python Karşılığı:
#  {
#    "isim": "Ali",        → str
#    "yas": 25,            → int
#    "hobiler": [...],     → list
#    "adres": {...}        → dict (iç içe sözlük)
#  }
# ============================================================

import requests
import json  # JSON işlemleri için

# -----------------------------------------------------------
# ÖRNEK 1: JSON yapısını inceleyelim
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 1: Ham JSON'ı görelim")
print("=" * 50)

cevap = requests.get("https://jsonplaceholder.typicode.com/users/1")

# .text → gelen veriyi düz metin olarak verir
print("Ham metin (text):")
print(cevap.text[:200], "...")  # İlk 200 karakter
print()

# .json() → metni Python sözlüğüne çevirir (bunu kullanıyoruz!)
veri = cevap.json()
print("Python sözlüğü (json()):")
print(type(veri))  # <class 'dict'>

# -----------------------------------------------------------
# ÖRNEK 2: İç içe JSON'ı okuma
# -----------------------------------------------------------

print()
print("=" * 50)
print("ÖRNEK 2: İç içe JSON okuma")
print("=" * 50)

kullanici = cevap.json()

# Düz değerler
print(f"İsim    : {kullanici['name']}")
print(f"Kullanıcı adı: {kullanici['username']}")
print(f"Email   : {kullanici['email']}")
print(f"Telefon : {kullanici['phone']}")
print(f"Website : {kullanici['website']}")

print()

# İç içe sözlük: adres bilgisi
adres = kullanici['address']           # Bu da bir sözlük!
print(f"Sokak   : {adres['street']}")
print(f"Şehir   : {adres['city']}")
print(f"Posta K.: {adres['zipcode']}")

# Daha derine: konum (lat/lng)
print(f"Enlem   : {adres['geo']['lat']}")
print(f"Boylam  : {adres['geo']['lng']}")

print()

# İç içe sözlük: şirket bilgisi
sirket = kullanici['company']
print(f"Şirket  : {sirket['name']}")

# -----------------------------------------------------------
# ÖRNEK 3: Liste içindeki JSON'ları işleme
# -----------------------------------------------------------

print()
print("=" * 50)
print("ÖRNEK 3: Liste içindeki JSON'ları döngüyle oku")
print("=" * 50)

cevap = requests.get("https://jsonplaceholder.typicode.com/posts")
gonderiler = cevap.json()   # Bu sefer bir LİSTE gelir

print(f"Toplam gönderi: {len(gonderiler)}")
print()
print("İlk 5 gönderi:")

for i, gonderi in enumerate(gonderiler[:5]):
    print(f"  [{gonderi['id']}] {gonderi['title']}")

# -----------------------------------------------------------
# ÖRNEK 4: JSON'u güzel yazdırma (indent)
# -----------------------------------------------------------

print()
print("=" * 50)
print("ÖRNEK 4: JSON'u okunabilir yazdırma")
print("=" * 50)

cevap = requests.get("https://jsonplaceholder.typicode.com/users/2")
veri = cevap.json()

# json.dumps() → Python sözlüğünü JSON formatında yazdırır
# indent=2      → 2 boşlukla girintili, okunması kolay
guzel_yazi = json.dumps(veri, indent=2, ensure_ascii=False)
print(guzel_yazi)

print()
print("Bir sonraki adım: 04_parametreli_istek.py")
print("=" * 50)
