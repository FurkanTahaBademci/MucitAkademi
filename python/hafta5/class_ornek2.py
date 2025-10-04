import datetime

class HesapMakinesi:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        self.sonuc = 0
        self.islem_tarihi = None
        self.islem_geçmişi = []

    def topla(self):
        self.sonuc = self.sayi1 + self.sayi2
        self.islem_tarihi = datetime.datetime.now()
        self.islem_geçmişi.append(("toplama", self.sonuc, self.islem_tarihi))
        return self.sonuc

    def cikar(self):
        self.sonuc = self.sayi1 - self.sayi2
        self.islem_tarihi = datetime.datetime.now()
        self.islem_geçmişi.append(("çıkarma", self.sonuc, self.islem_tarihi))
        return self.sonuc

    def carp(self):
        self.sonuc = self.sayi1 * self.sayi2
        self.islem_tarihi = datetime.datetime.now()
        self.islem_geçmişi.append(("çarpma", self.sonuc, self.islem_tarihi))
        return self.sonuc

    def bol(self):
        if self.sayi2 != 0:
            self.sonuc = self.sayi1 / self.sayi2
            self.islem_tarihi = datetime.datetime.now()
            self.islem_geçmişi.append(("bölme", self.sonuc, self.islem_tarihi))
            return self.sonuc
        else:
            return "Bir sayı sıfıra bölünemez."

    def islem_bilgisi(self):
        if self.islem_tarihi:
            return f"Son işlem: {self.sonuc} (Tarih: {self.islem_tarihi})"
        else:
            return "Henüz bir işlem yapılmadı."
    def islem_gecmisi_goster(self):
        return self.islem_geçmişi
    


hesap = HesapMakinesi(10, 5)
print("Toplama:", hesap.topla())
print(hesap.islem_bilgisi())
print("işlem geçmişi:", hesap.islem_gecmisi_goster())