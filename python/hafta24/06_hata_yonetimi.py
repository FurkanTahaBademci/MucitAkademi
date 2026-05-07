# ============================================================
#  HAFTA 24 - DERS 6: HATA YÖNETİMİ
# ============================================================
#
#  API çağrıları sırasında birçok şey yanlış gidebilir:
#
#  1. İnternet bağlantısı olmayabilir
#  2. Sunucu çökmüş olabilir (500 hatası)
#  3. Yanlış URL ya da endpoint girmiş olabilirsin (404)
#  4. Yetkisiz erişim (401, 403)
#  5. Çok fazla istek gönderdin (429 - Rate Limit)
#
#  İyi bir program bu durumları yakalamalı ve kullanıcıya
#  anlamlı bir mesaj göstermelidir.
#
# ------------------------------------------------------------
#  Hata yönetiminin 2 katmanı var:
#
#  1. HTTP Durum Kodu Kontrol  (cevap.status_code)
#     → Sunucu cevap verdi ama hata kodu gönderdi
#
#  2. try/except ile İstisna Yakalama
#     → İstek hiç gönderilemeди (bağlantı yok vs.)
# ============================================================

import requests

# -----------------------------------------------------------
# ÖRNEK 1: Durum koldu kontrolü
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 1: Durum kodu kontrolü")
print("=" * 50)

def kullanici_getir(kullanici_id):
    cevap = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{kullanici_id}"
    )
    
    # Durum koduna göre işlem yap
    if cevap.status_code == 200:
        return cevap.json()
    elif cevap.status_code == 404:
        print(f"Kullanıcı {kullanici_id} bulunamadı!")
        return None
    else:
        print(f"Beklenmedik hata: {cevap.status_code}")
        return None

# Var olan kullanıcı
k = kullanici_getir(3)
if k:
    print(f"Bulundu: {k['name']}")

# Var olmayan kullanıcı (JSONPlaceholder 1001 dönerse 404 verir)
k2 = kullanici_getir(999)

print()

# -----------------------------------------------------------
# ÖRNEK 2: raise_for_status() - kısa yol
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 2: raise_for_status() kullanımı")
print("=" * 50)

# raise_for_status() → Durum kodu 4xx veya 5xx ise otomatik hata fırlatır
# Bu sayede if/elif yazmak yerine try/except kullanabiliriz

def gonderi_getir_v2(gonderi_id):
    try:
        cevap = requests.get(
            f"https://jsonplaceholder.typicode.com/posts/{gonderi_id}"
        )
        cevap.raise_for_status()  # 4xx/5xx → HTTPError fırlatır
        return cevap.json()
    
    except requests.exceptions.HTTPError as hata:
        print(f"HTTP Hatası: {hata}")
        return None

gonderi = gonderi_getir_v2(5)
if gonderi:
    print(f"Başlık: {gonderi['title']}")

print()

# -----------------------------------------------------------
# ÖRNEK 3: Bağlantı hatalarını yakalama
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 3: Bağlantı hataları")
print("=" * 50)

def guvenli_get(url):
    """Her türlü hatayı yakalayan güvenli GET fonksiyonu"""
    try:
        cevap = requests.get(url, timeout=5)  # 5 saniye bekle, sonra vazgeç
        cevap.raise_for_status()
        return cevap.json()
    
    except requests.exceptions.ConnectionError:
        # İnternet yok, sunucu kapalı
        print("HATA: Bağlantı kurulamadı. İnternet bağlantınızı kontrol edin.")
        return None
    
    except requests.exceptions.Timeout:
        # Sunucu 5 saniye içinde cevap vermedi
        print("HATA: Sunucu zaman aşımına uğradı. Daha sonra tekrar deneyin.")
        return None
    
    except requests.exceptions.HTTPError as e:
        # 404, 500 gibi hata kodları
        print(f"HATA: Sunucu hata kodu döndürdü → {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        # Yukarıdakilere girmeyen her türlü requests hatası
        print(f"HATA: Beklenmedik bir sorun oluştu → {e}")
        return None

# Geçerli istek
veri = guvenli_get("https://jsonplaceholder.typicode.com/todos/1")
if veri:
    print(f"Görev: {veri['title']}")
    print(f"Tamamlandı mı: {veri['completed']}")

print()

# Geçersiz adres (bilerek hatalı yazıldı)
print("Geçersiz adrese istek:")
guvenli_get("https://bu-adres-yoktur-12345.com/api")

print()

# -----------------------------------------------------------
# ÖRNEK 4: Tam kapsamlı kullanım
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 4: Durum koduna göre renkli mesajlar")
print("=" * 50)

DURUM_MESAJLARI = {
    200: "OK - Her şey yolunda",
    201: "Created - Kayıt oluşturuldu",
    400: "Bad Request - Hatalı istek",
    401: "Unauthorized - Giriş yapman gerekiyor",
    403: "Forbidden - Bu işleme yetkin yok",
    404: "Not Found - İçerik bulunamadı",
    429: "Too Many Requests - Çok fazla istek",
    500: "Internal Server Error - Sunucu hatası",
}

def istek_yap_ve_raporla(url):
    try:
        cevap = requests.get(url, timeout=5)
        kod = cevap.status_code
        mesaj = DURUM_MESAJLARI.get(kod, f"Bilinmeyen kod: {kod}")
        
        print(f"URL  : {url}")
        print(f"Kod  : {kod}")
        print(f"Durum: {mesaj}")
        print()
        
        if cevap.ok:   # 200-299 arası → başarılı
            return cevap.json()
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"İstek başarısız: {e}")
        return None

istek_yap_ve_raporla("https://jsonplaceholder.typicode.com/posts/1")
istek_yap_ve_raporla("https://jsonplaceholder.typicode.com/posts/99999")

print("Bir sonraki adım: 07_hava_durumu_api.py")
print("=" * 50)
