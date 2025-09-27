"""19.	Asal Sayı Kontrolü Kullanıcıdan bir sayı alın. Bu sayının asal olup olmadığını for döngüsü kullanarak kontrol edin. (Asal sayı: Sadece 1'e ve kendisine bölünebilen sayıdır.)"""


sayi = int(input("Lütfen bir sayı giriniz: "))

if sayi > 1:
    for i in range(2, sayi):
        print("i: ",i)
        if (sayi % i) == 0:
            print(sayi, "asal sayı değildir.")
            break
    else:
        print(sayi, "asal sayıdır.")