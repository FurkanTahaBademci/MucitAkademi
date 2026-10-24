kisisel_bilgilerim = {
    "isim": "Furkan",
    "soyisim": "Yılmaz",
    "yas": 25,
    "sehir": "Istanbul"
}

print(kisisel_bilgilerim)
print(kisisel_bilgilerim["isim"])

kisisel_bilgilerim["meslek"] = "Mühendis"  # Yeni bir anahtar-değer çifti ekledik
print(kisisel_bilgilerim)

kisisel_bilgilerim["yas"] = 26  # Mevcut bir anahtarın değerini güncelledik
print(kisisel_bilgilerim["yas"])

for key in kisisel_bilgilerim:
    print( kisisel_bilgilerim[key])


print(kisisel_bilgilerim.items())  # Tüm anahtar-değer çiftlerini yazdırdı
print(kisisel_bilgilerim.keys())  # Tüm anahtarları yazdırdı
print(kisisel_bilgilerim.values())  # Tüm değerleri yazdırdı