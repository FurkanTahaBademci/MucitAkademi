import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX  

img = cv2.imread(r"C:\Users\furkan\Downloads\WhatsApp Image 2026-06-27 at 13.23.31.jpeg")   
# Normalize et ki parlaklık tutarlı olsun
image_norm = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
hsv = cv2.cvtColor(image_norm, cv2.COLOR_BGR2HSV)
# Beyaz/krem kağıt: düşük doygunluk (sarımsı sticky note dahil), yüksek parlaklık
beyaz_maske = cv2.inRange(hsv, np.array([0, 0, 150]), np.array([180, 80, 255]))
kernel = np.ones((20, 20), np.uint8)
beyaz_maske = cv2.morphologyEx(beyaz_maske, cv2.MORPH_CLOSE, kernel)

conturs, _ = cv2.findContours(beyaz_maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

gecis_kontrol = 0
referans_uzunluk = 0

img_h, img_w = img.shape[:2]
img_area = img_h * img_w

# Beyaz kareyi (referans) bul: kare şeklinde, makul boyutta kontur
en_buyuk_area = 0

for c in conturs:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    test = w / h if h != 0 else 0

    epsilon = 0.04 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    # Referans: görüntünün %0.1 ile %5'i arasında, kare şekilli
    if img_area * 0.001 < area < img_area * 0.05:
        print(f"[Aday] Alan: {int(area)}, Köşe: {len(approx)}, W/H: {test:.2f}")
        if 1.20 > test > 0.80 and 3 <= len(approx) <= 6 and area > en_buyuk_area:

            cv2.putText(img, "DETECT", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            referans_uzunluk = w
            en_buyuk_area = area
            gecis_kontrol = 1


if gecis_kontrol == 1:

    for c in conturs:
        area = cv2.contourArea(c)

        if area > 100:

            epsilon = 0.01 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)

            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            cv2.circle(img, (x + w, y), 5, (0, 0, 255), -1)
            cv2.circle(img, (x, y + h), 5, (0, 0, 255), -1)
            cv2.circle(img, (x + w, y + h), 5, (0, 0, 255), -1)

            # Referans kağıdın gerçek kenar uzunluğu (mm) -> buna göre ayarla
            REFERANS_MM = 30  # kağıdın gerçek kenar uzunluğu (örnek: 3x3 cm sticky note)

            en_gercek_uzunluk = int(REFERANS_MM * w) // referans_uzunluk
            boy_gercek_uzunluk = int(REFERANS_MM * h) // referans_uzunluk

            cv2.putText(img, (str(boy_gercek_uzunluk) + " mm"), (x, y + h // 2), font, 0.5, (0, 255, 0), 1)
            cv2.putText(img, (str(en_gercek_uzunluk) + " mm"), (x + w // 2, y), font, 0.5, (0, 255, 0), 1)

            print("x: ", x, " y: ", y, " w: ", w, " h: ", h)


ekran_genislik, ekran_yukseklik = 1280, 720
h_img, w_img = img.shape[:2]
olcek = min(ekran_genislik / w_img, ekran_yukseklik / h_img, 1.0)
goster = cv2.resize(img, (int(w_img * olcek), int(h_img * olcek)))

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img", goster.shape[1], goster.shape[0])
cv2.imshow("img", goster)
print("Referans Uzunluk: ", referans_uzunluk)
cv2.waitKey(0)
cv2.imwrite("output.jpg", img)   # args['output'] yerine direkt yol verdim, kendi yoluna göre değiştir
cv2.destroyAllWindows()