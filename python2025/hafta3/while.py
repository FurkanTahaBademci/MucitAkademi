sayi = 5

while sayi == 5:
    sayi += 1
    print("Sayı:", sayi)

#continue ve break

while True:
    sayi += 1
    if sayi == 7:
        continue  # sayi 7 olduğunda döngünün başına döner
    if sayi == 10:
        break  # sayi 10 olduğunda döngüden çıkar
    print("Sayı:", sayi)


