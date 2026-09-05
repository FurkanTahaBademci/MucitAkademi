import cv2
import easyocr

# 1. Resmi yükle ve EasyOCR ile oku
image_path = 'C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta18\\ocr.png'
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(image_path)

# 2. Resmi OpenCV ile aç (Çizim yapmak için)
img = cv2.imread(image_path)

for (bbox, text, prob) in result:
    # Koordinatları al (Tam sayı olmaları gerekir)
    top_left = tuple(map(int, bbox[0]))
    bottom_right = tuple(map(int, bbox[2]))

    # 3. Dikdörtgen çiz (Resim, SolÜst, SağAlt, Renk(BGR), Kalınlık)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

    # 4. Metni yaz (Resim, Metin, Konum, Font, Ölçek, Renk, Kalınlık)
    cv2.putText(img, text, (top_left[0], top_left[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# 5. Sonucu göster
cv2.imshow('OCR Sonucu', img)
cv2.waitKey(0) # Bir tuşa basana kadar pencereyi açık tutar
cv2.destroyAllWindows()

# İstersen sonucu bilgisayara da kaydedebilirsin
# cv2.imwrite('sonuc_cizili.png', img)