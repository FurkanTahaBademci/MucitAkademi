
class Havayolu:
    def __init__(self, ad, model,  rota, kapasite):
        self.ad = ad
        self.model = model
        self.rota = rota
        self.kapasite = kapasite
        self.ucus_gecmisi = []
        self.ücret = 0
        self.bilet_satis = 0
        self.maksimum_ucus_agirligi = 10000  # kg cinsinden

    def bilgileri_goster(self):
        print(f"Havayolu Adı: {self.ad}")
        print(f"Model: {self.model}")
        print(f"Kapasite: {self.kapasite} yolcu")

    def bilet_satis_yap(self, bilet_sayisi, bilet_ucreti):
        self.bilet_satis += bilet_sayisi
        self.ücret += bilet_sayisi * bilet_ucreti
        print(f"{bilet_sayisi} bilet satıldı. Toplam ücret: {self.ücret} TL")

    def ucus_ekle(self, rota, agirlik):
        if agirlik <= self.maksimum_ucus_agirligi:
            self.ucus_gecmisi.append(rota)
            print(f"{rota} rotasında uçuş eklendi.")
        else:
            print(
                f"Uçuş eklenemedi. Maksimum uçuş ağırlığı aşıldı: {self.maksimum_ucus_agirligi} kg")

    def ucus_gecmisini_goster(self):
        print("Uçuş Geçmişi:")
        for ucus in self.ucus_gecmisi:
            print(f"- {ucus}")

    def toplam_ücret(self):
        return self.ücret

    def toplam_bilet_satis(self):
        return self.bilet_satis

    def maksimum_ucus_agirligi_goster(self):
        return self.maksimum_ucus_agirligi

    def rota_guncelle(self, yeni_rota):
        self.ucus_gecmisi[-1] = yeni_rota
        print(f"Rota güncellendi: {self.ucus_gecmisi[-1]}")


ucus1 = Havayolu("THY", "Boeing 737", "İstanbul - Ankara", 180)

ucus1.bilgileri_goster()
ucus1.bilet_satis_yap(50, 300)
ucus1.ucus_gecmisini_goster()
ucus1.ucus_ekle("İstanbul - İzmir", 8000)
ucus1.ucus_ekle("İstanbul - New York", 9000)  # Ağırlık sınırını aşar
ucus1.ucus_gecmisini_goster()
ucus1.rota_guncelle("İstanbul - Antalya")
ucus1.ucus_gecmisini_goster()
