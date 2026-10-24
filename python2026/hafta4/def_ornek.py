def selam():
    print("Merhaba!")

def selam2():
    return "Merhaba!"

print(selam2())

def topla(a, b):
    return a + b

def carp(a, b):
    return a * b

def bol(a, b):
    return a / b

def cikar(a, b):
    return a - b

print(topla(3, 5))
print(cikar(6, 5))


def hosgeldiniz_mesaji(name,surname, age):
    print(f"Hoşgeldiniz, {name} {surname}! Yaşınız {age}.")
    
hosgeldiniz_mesaji("Furkan", "Bademci", 25)

def test():
    aa = "Furkan"
    bb = "Bademci"
    cc = 25
    return aa, bb, cc

a1, b1, c1 = test()
print(a1, b1, c1)
