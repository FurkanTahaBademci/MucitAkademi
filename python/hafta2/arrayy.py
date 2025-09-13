meyveler = ["elma", "armut", "muz"]

meyveler.append("çilek")  # liste sonuna ekler
print(meyveler)

meyveler2 = ["karpuz", "kavun"]
meyveler2.clear()  # listeyi temizler
print(f"meyveler2: {meyveler2}")

meyveler2 = meyveler.copy()  # listeyi kopyalar
print(f"meyveler2: {meyveler2}")

print("elma adeti : ",meyveler.count("elma"))  # listede kaç tane elma var



arabalar1 = ["BMW", "Mercedes", "Opel", "Mazda"]
arabalar2 = ["Renault", "Fiat", "Tofaş"]

arabalar1.extend(arabalar2)  # iki listeyi birleştirir
print(f"arabalar1: {arabalar1}")

arabalar1.index("Mercedes")  # Mercedes'in indexini verir
print(f"Mercedes index: {arabalar1.index('Mercedes')}")


arabalar1.insert(5, "furkan")  # 5. indexe furkan ekler
print(f"arabalar1: {arabalar1}")

arabalar1.pop(5) # 5. indexi siler
print(f"arabalar1: {arabalar1}")

arabalar1.remove("Mazda")  # Mazda'yı siler
print(f"arabalar1: {arabalar1}")

arabalar1.reverse()  # listeyi ters çevirir
print(f"arabalar1: {arabalar1}")

arabalar1.sort()  # listeyi alfabetik olarak sıralar
print(f"arabalar1: {arabalar1}")

kelimeler = ["furkan", "fulya", "faruk", "führe", "feyza"]

kelimeler.sort()  # listeyi alfabetik olarak sıralar
print(f"kelimeler: {kelimeler}")