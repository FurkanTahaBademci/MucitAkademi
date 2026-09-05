class Sinif:
    def __init__(self, isim, yas, notlar):
        self.isim = isim
        self.yas = yas
        self.notlar = notlar

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Notlar: {', '.join(map(str, self.notlar))}"

    def yas_arttir(self, miktar):
        self.yas += miktar
        return self.yas

    def isim_degistir(self, yeni_isim):
        self.isim = yeni_isim
        return self.isim

    def yas_getir(self):
        return self.yas

    def notlari_goster(self):
        return self.notlar

    def not_ekle(self, yeni_not):
        self.notlar.append(yeni_not)
        return self.notlar

    def ortalama_hesapla(self):
        if len(self.notlar) == 0:
            return 0
        return sum(self.notlar) / len(self.notlar)

    def notlari_sil(self):
        self.notlar = []
        return self.notlar


sinif = Sinif("Ahmet", 30, [85, 90, 78, 85, 12, 45])

print(sinif.bilgileri_goster())
print("Yaş arttırıldı:", sinif.yas_arttir(5))
print(sinif.bilgileri_goster())
print("İsim değiştirildi:", sinif.isim_degistir("Mehmet"))
print(sinif.bilgileri_goster())
print("Mevcut yaş:", sinif.yas_getir())
print("Notlar:", sinif.notlari_goster())
print("Yeni not eklendi:", sinif.not_ekle(95))
print("Notlar:", sinif.notlari_goster())
print("Ortalama not:", sinif.ortalama_hesapla())
print("Notlar silindi:", sinif.notlari_sil())
print("Notlar:", sinif.notlari_goster())
print("Ortalama not:", sinif.ortalama_hesapla())
