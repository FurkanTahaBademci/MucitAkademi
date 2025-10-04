
def count_a_in_text(text):
    count = text.lower().count('a')
    return count

# Örnek kullanım
example_text = "Ankara'da hava çok güzel."
result = count_a_in_text(example_text)
print("Metindeki 'a' sayısı:", result)