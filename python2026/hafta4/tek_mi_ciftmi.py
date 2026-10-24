
sayi = int(input("Bir sayı girin: "))


def tek_mi_cift_mi(sayi):
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"

print(tek_mi_cift_mi(sayi))
