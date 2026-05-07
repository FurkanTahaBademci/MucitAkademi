# ============================================================
#  HAFTA 24 - DERS 4: PARAMETRELİ İSTEK
# ============================================================
#
#  Parametreler, isteğe ek bilgi eklemek için kullanılır.
#  URL'de "?" işaretinden sonra yazılırlar.
#
#  ÖRNEK URL:
#  https://site.com/ara ? kelime=python & limit=10
#                        ─────────────   ─────────
#                        1. parametre    2. parametre
#
#  Yani URL şu anlama gelir:
#  "Python kelimesini ara, en fazla 10 sonuç getir"
#
#  Python'da bunu elle yazmak yerine params={} ile veririz.
#  requests kütüphanesi URL'i otomatik oluşturur.
# ============================================================

import requests

# -----------------------------------------------------------
# ÖRNEK 1: Belirli bir kullanıcının gönderilerini filtrele
# -----------------------------------------------------------

print("=" * 50)
print("ÖRNEK 1: Kullanıcıya göre gönderi filtrele")
print("=" * 50)

# Parametresiz → Tüm gönderiler gelir (100 tane)
# Parametreli  → Sadece istediğimiz kullanıcının gönderileri

parametreler = {
    "userId": 2   # Sadece 2 numaralı kullanıcının gönderilerini al
}

cevap = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=parametreler   # Parametreleri buraya ver
)

print(f"İstenen URL: {cevap.url}")
print()

gonderiler = cevap.json()
print(f"Kullanıcı 1'in gönderi sayısı: {len(gonderiler)}")
print()
print("Gönderiler:")
for g in gonderiler:
    print(f"  [{g['id']}] {g['title']}")

print()

# # -----------------------------------------------------------
# # ÖRNEK 2: Birden fazla parametre kullanma
# # -----------------------------------------------------------

# print("=" * 50)
# print("ÖRNEK 2: Yorumları filtrele")
# print("=" * 50)

# 5 numaralı gönderinin yorumlarını alalım
cevap = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 5}
)

print(f"İstenen URL: {cevap.url}")
print()

yorumlar = cevap.json()
print(f"5 numaralı gönderinin yorum sayısı: {len(yorumlar)}")
print()
print("Yorumlar:")
for y in yorumlar:
    print(f"  - {y['name']}")
    print(f"    {y['email']}")
    print()

# # -----------------------------------------------------------
# # ÖRNEK 3: Kanıtlayalım - URL'i elle yazmak ile aynı
# # -----------------------------------------------------------

# print("=" * 50)
# print("ÖRNEK 3: Karşılaştırma")
# print("=" * 50)

# # YÖNTEM A: params ile (önerilen)
# cevap_a = requests.get(
#     "https://jsonplaceholder.typicode.com/posts",
#     params={"userId": 2}
# )

# # YÖNTEM B: URL'e elle eklemek (okunması zor, hata riski var)
# cevap_b = requests.get(
#     "https://jsonplaceholder.typicode.com/posts?userId=2"
# )

# print(f"URL A: {cevap_a.url}")
# print(f"URL B: {cevap_b.url}")
# print(f"Sonuç aynı mı? {cevap_a.json() == cevap_b.json()}")

# # -----------------------------------------------------------
# # ÖRNEK 4: Kullanıcıdan parametre al (interaktif)
# # -----------------------------------------------------------

# print()
# print("=" * 50)
# print("ÖRNEK 4: İstediğin kullanıcının bilgilerini göster")
# print("=" * 50)

# try:
#     numara = int(input("Kullanıcı numarası gir (1-10): "))
    
#     cevap = requests.get(
#         f"https://jsonplaceholder.typicode.com/users/{numara}"
#     )
    
#     if cevap.status_code == 200:
#         k = cevap.json()
#         print(f"\nİsim   : {k['name']}")
#         print(f"Email  : {k['email']}")
#         print(f"Website: {k['website']}")
#         print(f"Şehir  : {k['address']['city']}")
#     else:
#         print(f"Kullanıcı bulunamadı! (Kod: {cevap.status_code})")

# except ValueError:
#     print("Geçersiz giriş! Sayı girmelisin.")

# print()
# print("Bir sonraki adım: 05_post_istegi.py")
# print("=" * 50)
