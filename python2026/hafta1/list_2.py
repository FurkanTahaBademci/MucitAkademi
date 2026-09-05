listem = [0,1, 2, 3, 4, 5]
print(listem[-1:])
print(listem[-2:])
print(listem[0:3])
print(listem[:3])  # aynı sonucu verir, başlangıçtan 3. indexe kadar
print(listem[3:])  # 3. indexten sona kadar
print(listem[::2])  # tüm listeyi yazdırır, 2'şer atlayarak
print(listem[1::2])  # tüm listeyi yazdırır, 1. indexten başlayarak 2'şer atlayarak
print(listem[::-1])  # tüm listeyi ters sırayla yazdırır