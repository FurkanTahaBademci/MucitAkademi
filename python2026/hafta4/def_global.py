def global_test():
    global aa, bb, cc
    aa = "Furkan"
    bb = "Bademci"
    cc = 25
    return "ben çalıştım"

print(global_test())

print(aa, bb, cc)


xx = 10

def deneme():
    global xx
    print(xx)
    xx = 11
    print(xx)

deneme()


