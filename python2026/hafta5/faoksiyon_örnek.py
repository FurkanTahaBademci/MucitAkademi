"""Süreç dıştan içe doğru şöyle akar:

siparis_olustur: Kullanıcı sepetini ve kart bilgilerini alır.

odeme_isle: Sipariş fonksiyonunun içinde çağrılır; bakiye ve kart doğrulama fonksiyonlarıyla haberleşir.

kart_gecerli_mi: Kart numarasının biçimini kontrol eder ve boolean döner.

bakiye_kontrol: Yeterli limit olup olmadığını teyit eder.
"""

import re

ürünlerim = [
    {"isim": "Elma", "fiyat": 5},
    {"isim": "Armut", "fiyat": 6},
    {"isim": "Muz", "fiyat": 7},
    {"isim": "Çilek", "fiyat": 8}
]

sepetim = []
kartlar = []

KART_DESENI = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{4}$")


# ---------- Yardımcı fonksiyonlar ----------

def sayı_oku(mesaj):
    """Geçerli ve negatif olmayan bir sayı girilene kadar sorar."""
    while True:
        try:
            değer = float(input(mesaj).replace(",", "."))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue
        if değer < 0:
            print("Değer negatif olamaz.")
            continue
        return değer


def ürün_bul(isim):
    for ürün in ürünlerim:
        if ürün["isim"].lower() == isim.lower():
            return ürün
    return None


def kart_bul(numara):
    for kart in kartlar:
        if kart["numara"] == numara:
            return kart
    return None


# ---------- Ürün işlemleri ----------

def ürün_ekle(isim, fiyat):
    if ürün_bul(isim):
        return False
    ürünlerim.append({"isim": isim, "fiyat": fiyat})
    return True


def ürünleri_yazdır():
    if not ürünlerim:
        print("Ürün yok.")
    for ürün in ürünlerim:
        print(f"{ürün['isim']} - {ürün['fiyat']} TL")


def ürün_sil(isim):
    global ürünlerim
    önceki = len(ürünlerim)
    ürünlerim = [ü for ü in ürünlerim if ü["isim"].lower() != isim.lower()]
    return len(ürünlerim) < önceki


# ---------- Sepet işlemleri ----------

def sepete_ekle(isim):
    """Ürünü katalogdaki fiyatıyla sepete ekler."""
    ürün = ürün_bul(isim)
    if not ürün:
        return False
    sepetim.append({"isim": ürün["isim"], "fiyat": ürün["fiyat"]})
    return True


def sepeti_yazdır():
    if not sepetim:
        print("Sepet boş.")
    for ürün in sepetim:
        print(f"{ürün['isim']} - {ürün['fiyat']} TL")
    print(f"Toplam: {sepet_toplam()} TL")


def sepet_toplam():
    return sum(ürün["fiyat"] for ürün in sepetim)


def sepetten_sil(isim):
    """Eşleşen ilk ürünü siler (aynı üründen birden fazla varsa yalnızca biri)."""
    for ürün in sepetim:
        if ürün["isim"].lower() == isim.lower():
            sepetim.remove(ürün)
            return True
    return False


# ---------- Kart işlemleri ----------

def kart_gecerli_mi(numara):
    """Kart numarası XXXX-XXXX-XXXX-XXXX biçiminde mi?"""
    return bool(KART_DESENI.match(numara))


def kart_ekle(numara, limit):
    if not kart_gecerli_mi(numara) or kart_bul(numara):
        return False
    kartlar.append({"numara": numara, "limit": limit})
    return True


def kartlari_yazdır():
    if not kartlar:
        print("Kayıtlı kart yok.")
    for kart in kartlar:
        print(f"{kart['numara']} - {kart['limit']} TL")


def kart_sil(numara):
    global kartlar
    önceki = len(kartlar)
    kartlar = [k for k in kartlar if k["numara"] != numara]
    return len(kartlar) < önceki


# ---------- Ödeme ve sipariş ----------

def bakiye_kontrol(kart, tutar):
    """Kartın limiti tutarı karşılıyor mu?"""
    return kart["limit"] >= tutar


def odeme_isle(numara, tutar):
    """Kartı doğrular, limiti kontrol eder ve tutarı düşer. (başarılı, mesaj) döner."""
    if not kart_gecerli_mi(numara):
        return False, "Kart numarası geçersiz (XXXX-XXXX-XXXX-XXXX)."
    kart = kart_bul(numara)
    if not kart:
        return False, "Kart bulunamadı."
    if not bakiye_kontrol(kart, tutar):
        return False, "Yetersiz limit."
    kart["limit"] -= tutar
    return True, "Ödeme başarılı."


def siparis_olustur(numara):
    """Sepeti ödemeye çevirir; başarılıysa sepeti boşaltır."""
    if not sepetim:
        print("Sepet boş, sipariş oluşturulamaz.")
        return False
    tutar = sepet_toplam()
    başarılı, mesaj = odeme_isle(numara, tutar)
    print(mesaj)
    if başarılı:
        print(f"Sipariş oluşturuldu. Ödenen tutar: {tutar} TL")
        sepetim.clear()
    return başarılı


kart_ekle("1234-5678-9876-5432", 1000)


def menü():
    while True:
        print("\n1. Ürünleri Yazdır")
        print("2. Ürün Ekle")
        print("3. Ürün Sil")
        print("4. Sepeti Yazdır")
        print("5. Sepete Ekle")
        print("6. Sepetten Sil")
        print("7. Kartları Yazdır")
        print("8. Kart Ekle")
        print("9. Kart Sil")
        print("10. Sipariş Oluştur (Ödeme Al)")
        print("0. Çıkış")

        secim = input("Seçiminizi yapın: ").strip()
        if secim == "1":
            ürünleri_yazdır()
        elif secim == "2":
            isim = input("Ürün ismi: ").strip()
            if not isim:
                print("İsim boş olamaz.")
                continue
            fiyat = sayı_oku("Ürün fiyatı: ")
            if not ürün_ekle(isim, fiyat):
                print("Bu isimde bir ürün zaten var.")
        elif secim == "3":
            if not ürün_sil(input("Silinecek ürün ismi: ").strip()):
                print("Ürün bulunamadı.")
        elif secim == "4":
            sepeti_yazdır()
        elif secim == "5":
            if not sepete_ekle(input("Sepete eklenecek ürün ismi: ").strip()):
                print("Ürün bulunamadı.")
        elif secim == "6":
            if not sepetten_sil(input("Sepetten silinecek ürün ismi: ").strip()):
                print("Ürün sepette yok.")
        elif secim == "7":
            kartlari_yazdır()
        elif secim == "8":
            numara = input("Kart numarası (XXXX-XXXX-XXXX-XXXX): ").strip()
            limit = sayı_oku("Kart limiti: ")
            if not kart_ekle(numara, limit):
                print("Kart eklenemedi (geçersiz biçim veya zaten kayıtlı).")
        elif secim == "9":
            if not kart_sil(input("Silinecek kart numarası: ").strip()):
                print("Kart bulunamadı.")
        elif secim == "10":
            siparis_olustur(input("Ödeme yapılacak kart numarası: ").strip())
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim")


if __name__ == "__main__":
    menü()
