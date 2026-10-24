yas = 19
egitim_durumu = "Lise"
egitim_durumu = str(input("Eğitim durumunuzu girin: ").lower())

if yas >= 18:
    print("Yaş şartı sağlandı.")
    if egitim_durumu in ["lise", "universite"]:
        print("Tebrikler, ehliyet başvurusunda bulunabilirsiniz!")
    else:
        print("Yaşınız tutuyor fakat en az lisede olmanız gerek.")

else:
    print(f"Ehliyet alamazsınız. {18 - yas} yıl daha beklemelisiniz.")