"""
Kitap Sınıfı
Bir Kitap sınıfı yazın. Özellikleri: kitap adı, yazar, sayfa sayısı, basım yılı.
Metotlar: kitabın bilgilerini göster, okunan sayfayı ekle, kalan sayfa sayısını hesapla.



"""


class Kitap:
    def __init__(self, kitap_adi, yazar, sayfa_sayisi, basim_yili):
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.basim_yili = basim_yili
        self.okunan_sayfa = 0

    def kitap_bilgileri(self):
        return f"Kitap Adı: {self.kitap_adi}, Yazar: {self.yazar}, Sayfa Sayısı: {self.sayfa_sayisi}, Basım Yılı: {self.basim_yili}"
    
    def okunan_sayfa_ekle(self, sayfa):
        if sayfa < 0:
            print("Okunan sayfa sayısı negatif olamaz.")
            return
        if self.okunan_sayfa + sayfa > self.sayfa_sayisi:
            print("Okunan sayfa sayısı toplam sayfa sayısını aşamaz.")
            return
        self.okunan_sayfa += sayfa

    def kalan_sayfa(self):
        return self.sayfa_sayisi - self.okunan_sayfa
    
    
kitap1 = Kitap("1984", "George Orwell", 328, 1949)
print(kitap1.kitap_bilgileri())

kitap1.okunan_sayfa_ekle(150)
kitap1.kitap_bilgileri()
print(f"Kalan Sayfa: {kitap1.kalan_sayfa()}")

