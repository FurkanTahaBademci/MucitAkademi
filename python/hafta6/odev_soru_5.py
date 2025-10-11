"""
Banka ATM Sistemi 
Bir ATM sınıfı yazın. 
• Özellikler: müşteri listesi (isim, hesap numarası, bakiye, şifre). 
• Metotlar: müşteri ekle, giriş yap, para yatır, para çek, bakiye sorgula. 
• Ek: Yanlış şifre 3 kez girilirse hesabı kilitleyen bir kontrol ekleyin. 
"""


class Atm:
    def __init__(self):
        self.musteri_listesi = []

    def musteri_ekle(self, isim, hesap_numarasi, bakiye, sifre):
        musteri = {
            "isim": isim,
            "hesap_numarasi": hesap_numarasi,
            "bakiye": bakiye,
            "sifre": sifre,
            "kilitli": False
        }
        self.musteri_listesi.append(musteri)

    def tum_musterilerin_isimleri(self):
        for musteri in self.musteri_listesi:
            print(musteri["isim"])

    def musteri_sil(self, hesap_numarasi):
        for musteri in self.musteri_listesi:
            if musteri["hesap_numarasi"] == hesap_numarasi:
                self.musteri_listesi.remove(musteri)
                print(f"Hesap numarası {hesap_numarasi} olan müşteri silindi.")
                return
        print(f"Hesap numarası {hesap_numarasi} olan müşteri bulunamadı.")

    def musteri_giris(self, hesap_numarasi, sifre):
        for musteri in self.musteri_listesi:
            if musteri["hesap_numarasi"] == hesap_numarasi and musteri["sifre"] == sifre:
                print(f"{musteri['isim']} olarak giriş yapıldı.")
                return musteri
        print("Hesap numarası veya şifre hatalı.")
        
    def para_yatir(self, musteri, miktar):
        if miktar > 0:
            musteri["bakiye"] += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {musteri['bakiye']} TL")
        else:
            print("Yatırılacak miktar pozitif olmalıdır.")
    
    def para_cek(self, musteri, miktar):
        if miktar > 0:
            if musteri["bakiye"] >= miktar:
                musteri["bakiye"] -= miktar
                print(f"{miktar} TL çekildi. Yeni bakiye: {musteri['bakiye']} TL")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Çekilecek miktar pozitif olmalıdır.")
    
    def bakiye_sorgula(self, musteri):
        print(f"Mevcut bakiye: {musteri['bakiye']} TL")

    def menü(self):
        while True:
            print("\nATM Menüsü:")
            print("1. Müşteri Ekle")
            print("2. Müşteri Sil")
            print("3. Giriş Yap")
            print("4. Çıkış")
            seçim = input("Seçiminizi yapın (1-4): ")
            
            if seçim == "1":
                isim = input("İsim: ")
                hesap_numarasi = input("Hesap Numarası: ")
                bakiye = float(input("Bakiye: "))
                sifre = input("Şifre: ")
                self.musteri_ekle(isim, hesap_numarasi, bakiye, sifre)
                print("Müşteri eklendi.")
                
            elif seçim == "2":
                hesap_numarasi = input("Silinecek Hesap Numarası: ")
                self.musteri_sil(hesap_numarasi)
                
            elif seçim == "3":
                hesap_numarasi = input("Hesap Numarası: ")
                sifre = input("Şifre: ")
                musteri = self.musteri_giris(hesap_numarasi, sifre)
                if musteri:
                    while True:
                        print("\n1. Para Yatır")
                        print("2. Para Çek")
                        print("3. Bakiye Sorgula")
                        print("4. Çıkış Yap")
                        alt_seçim = input("Seçiminizi yapın (1-4): ")
                        
                        if alt_seçim == "1":
                            miktar = float(input("Yatırılacak Miktar: "))
                            self.para_yatir(musteri, miktar)
                        elif alt_seçim == "2":
                            miktar = float(input("Çekilecek Miktar: "))
                            self.para_cek(musteri, miktar)
                        elif alt_seçim == "3":
                            self.bakiye_sorgula(musteri)
                        elif alt_seçim == "4":
                            print("Çıkış yapıldı.")
                            break
                        else:
                            print("Geçersiz seçim.")
                            
            elif seçim == "4":
                print("ATM'den çıkış yapıldı.")
                break
            else:
                print("Geçersiz seçim.")


atm1 = Atm()
atm1.menü()