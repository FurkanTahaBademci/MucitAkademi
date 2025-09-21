a = 5
b = 5
if a > b:
    # koşul doğruysa çalışır
    print("a büyüktür b")
elif a == b:
    # ilk koşul yanlış, bu doğruysa çalışır
    print("a eşittir b")
    print("a eşittir b")
elif a < b:
    # önceki koşullar yanlış, bu doğruysa çalışır
    print("a küçüktür b")

else:
    # kalan tüm durumlar
    print("a büyüktür veya eşittir b")
    
    
    


if a > b: print("a büyüktür b")
elif a == b: print("a eşittir b")
else: print("a küçüktür b")


a = 35
b = 33
c = 500
if a > b or a > c:  # veya (or) operatörü

  print("En az bir koşul doğru")
else:
    print("Hiçbir koşul doğru değil")
    
    
# and operatörü
if a < b and a < c:  # ve (and) operatörü
    print("Tüm koşullar doğru")
    
    
# not operatörü
if not(a < b and a < c):  # değil (not) operatörü
    print("En az bir koşul yanlış")