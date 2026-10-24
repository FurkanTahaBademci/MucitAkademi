ürünler = ["Elma", "Armut", "Muz", "Çilek"]
ürün_fiyatları = [5, 6, 7, 8]
kullanıcı_siparişleri = []
sipariş_tutarı = 0


def evet_mi(mesaj):
    """E/H cevabı gelene kadar sorar; E ise True döner."""
    while True:
        cevap = input(mesaj).strip().upper()
        if cevap in ("E", "H"):
            return cevap == "E"
        print("Lütfen E veya H girin.")


def ürün_seç():
    """Geçerli bir ürün numarası döner; geçersiz girişte None."""
    try:
        seçim = int(input(f"Lütfen bir ürün seçin (1-{len(ürünler)}): "))
    except ValueError:
        return None
    return seçim if 1 <= seçim <= len(ürünler) else None


devam = evet_mi("Sipariş oluşturmak ister misiniz? (E/H): ")
while devam:
    print("Ürünler:")
    for i, (ürün, fiyat) in enumerate(zip(ürünler, ürün_fiyatları), start=1):
        print(f"{i}. {ürün} - {fiyat} TL")

    seçim = ürün_seç()
    if seçim is None:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
    else:
        kullanıcı_siparişleri.append(ürünler[seçim - 1])
        sipariş_tutarı += ürün_fiyatları[seçim - 1]
        print(f"{ürünler[seçim - 1]} sepete eklendi.")

    devam = evet_mi("Başka bir ürün eklemek ister misiniz? (E/H): ")

if kullanıcı_siparişleri:
    print(f"Sepetinizdeki ürünler: {', '.join(kullanıcı_siparişleri)}")
    print(f"Toplam tutar: {sipariş_tutarı} TL")
    print("Siparişiniz tamamlandı.")
else:
    print("Sepetiniz boş, sipariş oluşturulmadı.")
