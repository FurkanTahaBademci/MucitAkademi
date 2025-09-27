def ornek_fonksiyonu(sayi):
    print("Bu bir örnek fonksiyondur.")
    print("Girilen sayı:", sayi)

ornek_fonksiyonu(10)

def topla(a, b):
    print("Toplama işlemi yapılıyor...")
    sayi = 20
    return a + b, sayi

sonuc, sayi = topla(5, 7)
print("Toplama sonucu:", sonuc)

print(sayi)
