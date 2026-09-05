"15.	Fibonacci Dizisinin İlk N Elemanı Kullanıcıdan bir N sayısı alın. Fibonacci dizisinin ilk N elemanını for döngüsü kullanarak ekrana yazdırın. (Fibonacci: 0, 1, 1, 2, 3, 5, 8...)"


n = int(input("Lütfen bir N sayısı giriniz: "))

a, b = 0, 1

fibonacci_dizisi = []
for _ in range(n):
    fibonacci_dizisi.append(a)
    a, b = b, a + b
    print("a:", a, "b:", b)
print("Fibonacci dizisinin ilk", n, "elemanı:", fibonacci_dizisi)
