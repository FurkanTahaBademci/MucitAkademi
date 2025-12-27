import os
import random
from PIL import Image


def dinamik_cozunurluk_uret(resim, temel_ad, hedef_klasor, varyasyon_sayisi=20):
    """Resmi rastgele ölçeklerde yeniden boyutlandırarak kaydeder."""
    genislik, yukseklik = resim.size

    # Farklı algoritmalar pHash sonucunu hafif etkileyebilir, bunları da çeşitlendirelim
    resampling_metodlari = [
        Image.Resampling.LANCZOS,
        Image.Resampling.BILINEAR,
        Image.Resampling.BICUBIC,
        Image.Resampling.NEAREST
    ]

    for i in range(varyasyon_sayisi):
        # 0.1 (çok küçük) ile 2.0 (iki kat büyük) arasında rastgele bir katsayı
        oran = random.uniform(0.9, 4.0)

        yeni_g = int(genislik * oran)
        yeni_y = int(yukseklik * oran)

        # Rastgele bir yeniden örnekleme metodu seç
        metod = random.choice(resampling_metodlari)

        temp_img = resim.resize((yeni_g, yeni_y), resample=metod)
        
        # Eğer resim RGBA modundaysa (alfa kanalı varsa), RGB'ye çevir
        if temp_img.mode == 'RGBA':
            # Beyaz arkaplan ile alpha kanalını birleştir
            rgb_img = Image.new('RGB', temp_img.size, (255, 255, 255))
            rgb_img.paste(temp_img, mask=temp_img.split()[-1])  # Alpha kanalını mask olarak kullan
            temp_img = rgb_img

        # Dosya adında çözünürlüğü belirtelim (takip kolaylığı için)
        kayit_adi = f"{temel_ad}_{yeni_g}x{yeni_y}_v{i}.jpg"
        temp_img.save(os.path.join(hedef_klasor, kayit_adi),
                      quality=random.randint(70, 95))


def test_verisi_olustur(kaynak_klasor, cikis_klasor, her_resimden_kac_tane=15):
    """Klasördeki her resmi alır ve farklı çözünürlüklerde kopyalarını üretir."""
    if not os.path.exists(cikis_klasor):
        os.makedirs(cikis_klasor)

    dosyalar = [f for f in os.listdir(
        kaynak_klasor) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not dosyalar:
        print(f"Hata: {kaynak_klasor} klasöründe resim bulunamadı.")
        return

    for dosya in dosyalar:
        yol = os.path.join(kaynak_klasor, dosya)
        temel_ad = os.path.splitext(dosya)[0]

        with Image.open(yol) as img:
            # Eğer resim RGBA modundaysa (alfa kanalı varsa), RGB'ye çevir
            if img.mode == 'RGBA':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1])
                img = rgb_img
            
            print(f"İşleniyor: {dosya} (Orijinal: {img.size})")
            dinamik_cozunurluk_uret(
                img, temel_ad, cikis_klasor, her_resimden_kac_tane)

    print(
        f"\nTamamlandı! '{cikis_klasor}' klasöründe bolca farklı çözünürlükte test verisi var.")

# --- KULLANIM ---
# 'referans' klasöründeki her bir resimden 30'ar tane farklı çözünürlükte kopya üretir
test_verisi_olustur("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta16\\image", "karisik_cozunurluk_testi", her_resimden_kac_tane=15)
