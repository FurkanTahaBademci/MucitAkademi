# ============================================================
#  HAFTA 24 - DERS 7: GERÇEK API - HAVA DURUMU
# ============================================================
#
#  Artık öğrendiğimiz her şeyi gerçek bir API'de kullanalım!
#
#  Open-Meteo API kullanacağız:
#  - Tamamen ÜCRETSİZ
#  - API anahtarı (key) GEREKMİYOR
#  - Gerçek hava durumu verileri
#  - Adres: https://open-meteo.com
#
# ------------------------------------------------------------
#  Nasıl çalışır?
#
#  1. Şehrin koordinatlarını (enlem, boylam) buluyoruz
#     → Bunun için "geocoding" API kullanacağız
#
#  2. Koordinatlarla hava durumu sorguluyoruz
#     → weather API'sine koordinat + istediğimiz veriler
#
# ------------------------------------------------------------
#  Kullanacağımız API endpoint'leri:
#
#  Geocoding (şehir → koordinat):
#  https://geocoding-api.open-meteo.com/v1/search?name=Istanbul
#
#  Hava durumu (koordinat → hava):
#  https://api.open-meteo.com/v1/forecast?latitude=41&longitude=29&...
# ============================================================

import requests

# -----------------------------------------------------------
# ADIM 1: Şehrin koordinatlarını bul
# -----------------------------------------------------------

def sehir_koordinat_bul(sehir_adi):
    """Şehir adından enlem ve boylam koordinatlarını döndürür"""
    
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametreler = {
        "name": sehir_adi,
        "count":5,
        "language": "tr",     # Türkçe sonuçlar
        "format": "json"
    }
    
    try:
        cevap = requests.get(url, params=parametreler, timeout=10)
        cevap.raise_for_status()
        veri = cevap.json()
        
        if "results" in veri and len(veri["results"]) > 0:
            sonuc = veri["results"][0]
            return {
                "isim": sonuc["name"],
                "ulke": sonuc.get("country", ""),
                "enlem": sonuc["latitude"],
                "boylam": sonuc["longitude"],
                "yukseklik": sonuc.get("elevation", 0)
            }
        else:
            print(f"'{sehir_adi}' şehri bulunamadı.")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Koordinat alınamadı: {e}")
        return None






# # -----------------------------------------------------------
# # ADIM 2: Hava durumunu al
# # -----------------------------------------------------------

def hava_durumu_al(enlem, boylam):
    """Koordinata göre anlık hava durumu bilgilerini döndürür"""
    
    url = "https://api.open-meteo.com/v1/forecast"
    parametreler = {
        "latitude": enlem,
        "longitude": boylam,
        "current": [           # Anlık veriler
            "temperature_2m",       # Sıcaklık (°C)
            "relative_humidity_2m", # Nem (%)
            "apparent_temperature", # Hissedilen sıcaklık
            "wind_speed_10m",       # Rüzgar hızı (km/s)
            "precipitation",        # Yağış (mm)
            "weather_code",         # Hava kodu
        ],
        "timezone": "Europe/Istanbul",
        "forecast_days": 1
    }
    
    try:
        cevap = requests.get(url, params=parametreler, timeout=10)
        cevap.raise_for_status()
        return cevap.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Hava durumu alınamadı: {e}")
        return None

# -----------------------------------------------------------
# Yardımcı: Hava kodunu Türkçeye çevir
# -----------------------------------------------------------

def hava_kodu_acikla(kod):
    """WMO hava kodu → Türkçe açıklama"""
    kodlar = {
        0: "Açık",
        1: "Çoğunlukla açık",
        2: "Parçalı bulutlu",
        3: "Bulutlu",
        45: "Sisli",
        48: "Kırağılı sis",
        51: "Hafif çiseleyen yağmur",
        53: "Orta çiseleyen yağmur",
        55: "Yoğun çiseleyen yağmur",
        61: "Hafif yağmur",
        63: "Orta yağmur",
        65: "Şiddetli yağmur",
        71: "Hafif kar",
        73: "Orta kar",
        75: "Yoğun kar",
        80: "Hafif sağanak",
        81: "Orta sağanak",
        82: "Şiddetli sağanak",
        95: "Thunderstorm",
        99: "Dolu ile fırtına",
    }
    return kodlar.get(kod, f"Bilinmeyen ({kod})")

# -----------------------------------------------------------
# ADIM 3: Sonuçları güzel göster
# -----------------------------------------------------------

def hava_raporu_goster(sehir):
    """Şehir adı alır, hava durumu raporunu yazdırır"""
    
    print(f"\n'{sehir}' için hava durumu aranıyor...")
    print("-" * 40)
    
    # Koordinat bul
    konum = sehir_koordinat_bul(sehir)
    if not konum:
        return
    
    # Hava durumunu al
    hava = hava_durumu_al(konum["enlem"], konum["boylam"])
    if not hava:
        return
    
    # Anlık verilere ulaş
    anlik = hava["current"]
    
    # Raporu yazdır
    print(f"Şehir         : {konum['isim']}, {konum['ulke']}")
    print(f"Koordinatlar  : {konum['enlem']:.2f}N, {konum['boylam']:.2f}E")
    print(f"Yükseklik     : {konum['yukseklik']:.0f} m")
    print()
    print(f"Hava Durumu   : {hava_kodu_acikla(anlik['weather_code'])}")
    print(f"Sıcaklık      : {anlik['temperature_2m']} °C")
    print(f"Hissedilen    : {anlik['apparent_temperature']} °C")
    print(f"Nem           : %{anlik['relative_humidity_2m']}")
    print(f"Rüzgar        : {anlik['wind_speed_10m']} km/s")
    print(f"Yağış         : {anlik['precipitation']} mm")
    print(f"Güncelleme    : {anlik['time']}")

# -----------------------------------------------------------
# ÇALIŞTIR
# -----------------------------------------------------------

print("=" * 50)
print("  GERÇEK ZAMANLI HAVA DURUMU UYGULAMASI")
print("  (open-meteo.com API - Ücretsiz, key gereksiz)")
print("=" * 50)

# Bazı şehirler için hava durumu
sehirler = ["Sakarya", "Izmir"]

for sehir in sehirler:
    hava_raporu_goster(sehir)
    print()

# # -----------------------------------------------------------
# # İnteraktif kullanım
# # -----------------------------------------------------------

# print("=" * 50)
# print("Kendi şehrini dene!")
# print("=" * 50)

# girdi = input("Şehir adı gir (çıkmak için Enter): ").strip()
# if girdi:
#     hava_raporu_goster(girdi)

# print()
# print("Bir sonraki adım: 08_kendi_api.py")
# print("=" * 50)
