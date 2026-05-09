
import requests
import json

# -----------------------------------------------------------
# ÖRNEK 1: Yeni gönderi oluştur (POST)
# -----------------------------------------------------------
# Göndermek istediğimiz veri (Python sözlüğü)
yeni_gonderi = {
    "ad": "Furkan",
    "email": "furkan@example.com",
    "yas": 30,
    "id": 9999  # ID sunucu tarafından atanacak, burada sadece örnek için 0 verdik
}

cevap = requests.post(
    "http://192.168.5.81:5000/kullanicilar",
    json=yeni_gonderi   # json= ile veriyi otomatik JSON formatında gönderir
)

print(f"Durum kodu: {cevap.status_code}")  # 201 = Created (oluşturuldu)
print()

# Sunucu oluşturduğu kaydı geri döner (ID ile birlikte)
olusturulan = cevap.json()
print("Sunucunun döndürdüğü veri:")
print(json.dumps(olusturulan, indent=4))  # JSON'u güzel formatta yazdır

print()