def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Hata: Bir sayı sıfıra bölünemez."
    return a / b

def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    while True:
        secim = input("Bir işlem seçin (1/2/3/4) veya çıkmak için 'q' tuşuna basın: ")

        if secim == 'q':
            print("Hesap makinesinden çıkılıyor...")
            break

        if secim in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Birinci sayıyı girin: "))
                num2 = float(input("İkinci sayıyı girin: "))
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı girin.")
                continue

            if secim == '1':
                print(f"{num1} + {num2} = {topla(num1, num2)}")
            elif secim == '2':
                print(f"{num1} - {num2} = {cikar(num1, num2)}")
            elif secim == '3':
                print(f"{num1} * {num2} = {carp(num1, num2)}")
            elif secim == '4':
                sonuc = bol(num1, num2)
                print(f"{num1} / {num2} = {sonuc}")
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            
            
hesap_makinesi()