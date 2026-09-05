# ============================================================
#  HAFTA 24 - DERS 1: API NEDİR?
# ============================================================
#
#  API = Application Programming Interface
#       (Uygulama Programlama Arayüzü)
#
# ------------------------------------------------------------
#  GERÇEK HAYAT ÖRNEĞİ İLE ANLAYALIM:
#
#  Bir restorana gittiğini düşün.
#
#    SEN          →  Müşteri (uygulama)
#    GARSON       →  API
#    MUTFAK       →  Sunucu (server)
#
#  1. Menüye bakarak ne istediğini söylersin  → İSTEK (Request)
#  2. Garson mutfağa iletir
#  3. Mutfak yemeği hazırlar
#  4. Garson sana getirir                    → CEVAP (Response)
#
#  Sen mutfağa girip doğrudan yemek yapmıyorsun.
#  Garson (API) senin için bu işi hallediyor!
#
# ------------------------------------------------------------
#  Günlük hayatta API örnekleri:
#
#  - Hava durumu uygulaması → Meteoroloji sunucusundan API ile veri çeker
#  - Google Haritalar        → Harita verilerini API ile alır
#  - Instagram giriş butonu → Instagram'ın API'sini kullanır
#  - Ödeme sistemleri        → Banka API'si ile para transferi yapar
#
# ------------------------------------------------------------
#  API nasıl çalışır?
#
#  [Uygulama] ---(istek)---> [İnternet] ---> [Sunucu]
#  [Uygulama] <--(cevap)--- [İnternet] <--- [Sunucu]
#
#  İstek (Request) : "Bana İstanbul'un hava durumunu ver"
#  Cevap (Response): {"şehir": "İstanbul", "sıcaklık": 22}
#
# ------------------------------------------------------------
#  API'lerde kullanılan HTTP metodları:
#
#  GET    → Veri AL         (örn: kullanıcı bilgisini getir)
#  POST   → Veri GÖNDER     (örn: yeni kullanıcı oluştur)
#  PUT    → Veriyi GÜNCELLE (örn: kullanıcı adını değiştir)
#  DELETE → Veriyi SİL      (örn: hesabı sil)
#
# ------------------------------------------------------------
#  Bu haftaki yol haritası:
#
#  01_api_nedir.py          → ŞU AN BURADASIN - API nedir?
#  02_ilk_get_istegi.py     → İlk GET isteği nasıl yapılır?
#  03_json_anlama.py        → Gelen JSON veriyi nasıl okuruz?
#  04_parametreli_istek.py  → İsteğe parametre eklemek
#  05_post_istegi.py        → POST ile veri göndermek
#  06_hata_yonetimi.py      → Hataları nasıl yönetiriz?
#  07_hava_durumu_api.py    → Gerçek bir API kullanımı
#  08_kendi_api.py          → Kendi API'mizi yazalım!
#
# ------------------------------------------------------------

print("=" * 50)
print("  API'ye HOŞ GELDİN!")
print("=" * 50)
print()
print("API = Application Programming Interface")
print("    = Uygulama Programlama Arayüzü")
print()
print("Kısaca: İki yazılımın birbiyle konuşma şekli.")
print()
print("Nasıl çalışır?")
print("  1. Sen bir İSTEK yaparsın  (request)")
print("  2. Sunucu sana CEVAP verir (response)")
print()
print("Tıpkı bir restorandaki garson gibi!")
print("  Sen     = Uygulama")
print("  Garson  = API")
print("  Mutfak  = Sunucu")
print()
print("Bir sonraki adım: 02_ilk_get_istegi.py")
print("=" * 50)
