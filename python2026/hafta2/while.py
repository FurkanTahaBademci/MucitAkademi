liste = [0, 1, 2, 3, 4]
sayac = 0

while sayac <= len(liste):
    print("Bu bir while döngüsüdür.")
    sayac += 1
    print(sayac)

sayac = 0
while True:
    print("Bu bir sonsuz while döngüsüdür.")
    sayac += 1
    if sayac >= len(liste):
        break
