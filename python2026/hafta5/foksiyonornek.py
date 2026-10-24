calisan_maas_dict = {}

def calisanlari_yazdir(calisan_maas_dict):
    for calisan in calisan_maas_dict:
        print(calisan)


def calisan_sayisini_yazdir(calisan_maas_dict):
    print("Çalışan sayısı:", len(calisan_maas_dict))


# çalışanların maaşını ekleyelim
def calisan_maasini_yazdir(calisan, maas):
    print(f"{calisan} maaşı: {maas} TL")

def maas_ekle(calisan_maas_dict, calisan, maas):
    calisan_maas_dict[calisan] = maas


def maas_artir(calisan_maas_dict, calisan, miktar):
    if calisan in calisan_maas_dict:
        calisan_maas_dict[calisan] += miktar
    else:
        print(f"{calisan} bulunamadı.")


def toplu_maas_artir(calisan_maas_dict, miktar):
    for calisan in calisan_maas_dict:
        calisan_maas_dict[calisan] += miktar


def toplu_maas_ayarla(calisan_maas_dict, maas):
    for calisan in calisan_maas_dict:
        calisan_maas_dict[calisan] = maas

def vergi_hesapla(calisan_maas_dict, vergi_orani):
    for calisan in calisan_maas_dict:
        calisan_maas_dict[calisan] -= calisan_maas_dict[calisan] * vergi_orani / 100


def calisma_gün_ekle(calisan_maas_dict, calisma_gunleri, calisan, gün):
    if calisan in calisan_maas_dict:
        calisma_gunleri[calisan] = calisma_gunleri.get(calisan, 0) + gün
    else:
        print(f"{calisan} bulunamadı.")


def en_cok_calisani_yazdır(calisma_gunleri):
    if calisma_gunleri:
        en_cok_calisan = max(calisma_gunleri, key=calisma_gunleri.get)
        print(f"En çok çalışan: {en_cok_calisan} ({calisma_gunleri[en_cok_calisan]} gün)")
    else:
        print("Çalışma günleri bilgisi bulunamadı.")


maas_ekle(calisan_maas_dict, "Ahmet", 5000)
maas_ekle(calisan_maas_dict, "Mehmet", 4500)
maas_ekle(calisan_maas_dict, "Ayşe", 4800)
maas_ekle(calisan_maas_dict, "Fatma", 4700)

toplu_maas_artir(calisan_maas_dict, 200)
print(calisan_maas_dict)

toplu_maas_ayarla(calisan_maas_dict, 6000)
print(calisan_maas_dict)


vergi_hesapla(calisan_maas_dict, 20)
print(calisan_maas_dict)


calisma_gunleri = {}
calisma_gün_ekle(calisan_maas_dict, calisma_gunleri, "Ahmet", 5)
calisma_gün_ekle(calisan_maas_dict, calisma_gunleri, "Mehmet", 10)
print(calisan_maas_dict)
print(calisma_gunleri)

en_cok_calisani_yazdır(calisma_gunleri)
