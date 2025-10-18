f = open("test.txt", "r", encoding="utf-8")
print(f.read())

# yazma işlemi
f = open("test.txt", "a", encoding="utf-8")
f.write("Merhaba Dünya\n")
f.write("Python ile dosya işlemleri\n")
f.close()