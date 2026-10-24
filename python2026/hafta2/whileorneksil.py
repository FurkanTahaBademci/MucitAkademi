ornek_seri = [1, 2, 3, 4, 5]

i = 0
while i < len(ornek_seri):
    print(ornek_seri[i])
    i += 1

for eleman in ornek_seri:
    if eleman % 2 == 0:
        print(eleman)
    else:
        print("Tek sayı")


for eleman in ornek_seri:
    print("Eleman:", eleman)
    if eleman == 3:
        break
    print("Eleman:", eleman)
