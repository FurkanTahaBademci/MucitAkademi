array = [54, 67, 423, 453, 123]

for i in array:
    print("Sayı:", i)


#range fonksiyonu
for i in range(5):

    print("Sayı:", i)
    if i == 3:
        print("Sayı 3 oldu, döngüden çıkılıyor.")
        break
    
    
#continue ve break


for i in range(10):
    if i == 3:
        continue  # i 3 olduğunda döngünün başına döner
    if i == 7:
        break  # i 7 olduğunda döngüden çıkar
    print("Sayı:", i)
    
    
    
print("#################################")

fruits = ["apple", "banana", "cherry"]
for meyve in fruits:
  print(meyve)
  if meyve == "banana":
    print("Muz bulundu, döngüden çıkılıyor.")
    break


#deger = input("bir kelime girin ")
#print("Girdiğiniz kelime:", deger)


array = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]


for alt_array in array:
    for eleman in alt_array:
        print("Eleman:", eleman)
    if eleman == 3:
        print("Eleman 3 bulundu, iç döngüden çıkılıyor.")
        break


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  
  if x == "year":
      print("Yıl anahtarına ulaşıldı.")
      print("Değeri:", thisdict[x])
  