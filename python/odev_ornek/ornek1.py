"""7.	Hafta Sonu mu, Hafta İçi mi? Kullanıcıdan günün adını (Pazartesi, Salı vb.) girmesini isteyin. Girilen gün "Cumartesi" veya "Pazar" ise "İyi tatiller!", diğer günlerden biriyse "İyi çalışmalar!" yazdırın."""

gunler = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]

gun = input("Lütfen günün adını giriniz: ")

gun = gun.lower()

if gun in gunler:
    if gun == "cumartesi" or gun == "pazar":
        print("İyi tatiller!")
    else:
        print("İyi çalışmalar!")
else:
    print("Geçersiz gün adı.")
