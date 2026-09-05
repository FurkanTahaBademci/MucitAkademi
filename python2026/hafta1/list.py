liste = [1,2,3,4,5,5,"eymen"]
print(liste)
print(type(liste))
print(len(liste))
liste.append("furkan")  # sondan ekleme yapıyor
print(liste)
liste.remove(5)  # 1 tane siliyor, ilk bulduğu 5'i siler
print(liste)
liste.pop()  # sondan eleman çıkarır
print(liste)

liste.insert(2, "emir")  # belirli bir index'e ekleme yapar
print(liste)

print(liste[5])  # 5. indexteki elemanı yazdırır

print(liste[-1])  # sondan 1. elemanı yazdırır







