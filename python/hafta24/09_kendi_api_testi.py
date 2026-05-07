# ============================================================
#  HAFTA 24 - BONUS: KENDİ API'Mİ TEST ET
# ============================================================
#
#  Bu dosya, 08_kendi_api.py ile yazdığımız API'yi test eder.
#
#  ÖNCE 08_kendi_api.py'yi çalıştır (ayrı terminal)!
#  Sonra bu dosyayı çalıştır.
#
#  Yani iki terminal açık olmalı:
#  Terminal 1: python 08_kendi_api.py   ← sunucu
#  Terminal 2: python 09_kendi_api_testi.py ← test
# ============================================================

import requests
import json

BASE_URL = "http://127.0.0.1:5000"  # Sunucumuzun adresi

def baslik(metin):
    print()
    print("=" * 50)
    print(f"  {metin}")
    print("=" * 50)

# -----------------------------------------------------------
# TEST 1: Ana sayfa
# -----------------------------------------------------------

baslik("TEST 1: Ana sayfaya GET isteği")

cevap = requests.get(f"{BASE_URL}/")
print(f"Durum: {cevap.status_code}")
print(json.dumps(cevap.json(), indent=2, ensure_ascii=False))

# -----------------------------------------------------------
# TEST 2: Tüm kullanıcıları listele
# -----------------------------------------------------------

baslik("TEST 2: Tüm kullanıcıları listele")

cevap = requests.get(f"{BASE_URL}/kullanicilar")
veri = cevap.json()
print(f"Durum: {cevap.status_code}")
print(f"Toplam kullanıcı: {veri['toplam']}")
for k in veri["kullanicilar"]:
    print(f"  [{k['id']}] {k['ad']} - {k['email']}")

# -----------------------------------------------------------
# TEST 3: Belirli bir kullanıcıyı getir
# -----------------------------------------------------------

baslik("TEST 3: 2 numaralı kullanıcıyı getir")

cevap = requests.get(f"{BASE_URL}/kullanicilar/2")
print(f"Durum: {cevap.status_code}")
k = cevap.json()
print(f"İsim : {k['ad']}")
print(f"Email: {k['email']}")
print(f"Yaş  : {k['yas']}")

# -----------------------------------------------------------
# TEST 4: Olmayan kullanıcı
# -----------------------------------------------------------

baslik("TEST 4: Olmayan kullanıcı (404 testi)")

cevap = requests.get(f"{BASE_URL}/kullanicilar/999")
print(f"Durum: {cevap.status_code}")  # 404 bekliyoruz
print(f"Hata : {cevap.json()['hata']}")

# -----------------------------------------------------------
# TEST 5: Yeni kullanıcı ekle (POST)
# -----------------------------------------------------------

baslik("TEST 5: Yeni kullanıcı ekle (POST)")

yeni = {
    "ad": "Zeynep Çelik",
    "email": "zeynep@example.com",
    "yas": 21
}

cevap = requests.post(f"{BASE_URL}/kullanicilar", json=yeni)
print(f"Durum: {cevap.status_code}")  # 201 bekliyoruz
sonuc = cevap.json()
print(f"Mesaj: {sonuc['mesaj']}")
print(f"Yeni kullanıcı ID: {sonuc['kullanici']['id']}")

# Şimdi listeye eklendi mi kontrol et
cevap2 = requests.get(f"{BASE_URL}/kullanicilar")
print(f"Güncel kullanıcı sayısı: {cevap2.json()['toplam']}")

# -----------------------------------------------------------
# TEST 6: Hesap makinesi
# -----------------------------------------------------------

baslik("TEST 6: Hesap makinesi API'si")

cevap = requests.get(f"{BASE_URL}/hesapla", params={"sayi1": 15, "sayi2": 4})
print(f"Durum: {cevap.status_code}")
sonuc = cevap.json()
print(f"Toplam  : {sonuc['toplam']}")
print(f"Fark    : {sonuc['fark']}")
print(f"Çarpım  : {sonuc['carpim']}")
print(f"Bölüm   : {sonuc['bolum']}")

# -----------------------------------------------------------
# ÖZET
# -----------------------------------------------------------

baslik("TÜM TESTLER TAMAMLANDI!")
print("Tebrikler! Hem API yazdın, hem de test ettin.")
print()
print("Öğrendiklerin:")
print("  ✓ API nedir")
print("  ✓ GET isteği yapmak")
print("  ✓ JSON okumak")
print("  ✓ Parametreli istek")
print("  ✓ POST isteği yapmak")
print("  ✓ Hata yönetimi")
print("  ✓ Gerçek bir API kullanmak")
print("  ✓ Kendi API'ni yazmak")
print("=" * 50)
