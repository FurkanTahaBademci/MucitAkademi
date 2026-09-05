import numpy as np
import cv2
import imutils
from imutils import contours

# 20 Soru için örnek cevap anahtarı (0:A, 1:B, 2:C, 3:D, 4:E)
ANSWER_KEY = {
    1: 2, 2: 3, 3: 1, 4: 3, 5: 4,
    6: 0, 7: 1, 8: 2, 9: 3, 10: 4,
    11: 0, 12: 1, 13: 2, 14: 3, 15: 4,
    16: 0, 17: 1, 18: 2, 19: 3, 20: 4
}


def process_omr_column(image_roi, answer_key, start_q):
    """Belirli bir soru sütununu (ROI) işler ve sonuçları döndürür."""
    gray = cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # CRITICAL: THRESH_BINARY_INV kullanıyoruz ki yazılar/dolu alanlar beyaz, arkaplan siyah olsun
    thresh = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    questionCnts = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        # Yuvarlak tespiti için boyut ve en-boy oranını kontrol et
        if w >= 25 and h >= 25 and ar >= 0.85 and ar <= 1.15:
            questionCnts.append(c)

    # Eğer eksik yuvarlak bulunduysa hata ver
    if len(questionCnts) != 50:  # 10 soru * 5 şık = 50 yuvarlak
        print(
            f"[UYARI] Sütunda 50 yuvarlak bulunamadı, {len(questionCnts)} adet bulundu. Görüntü kalitesini kontrol edin.")
        return 0, image_roi

    # Soruları yukarıdan aşağıya sırala
    questionCnts = contours.sort_contours(
        questionCnts, method="top-to-bottom")[0]
    correct_count = 0

    for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
        # Her satırdaki 5 şıkkı soldan sağa sırala (A, B, C, D, E)
        cnts_row = contours.sort_contours(
            questionCnts[i:i + 5], method="left-to-right")[0]
        bubbled = None

        for (j, c) in enumerate(cnts_row):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)

            # Maske ile threshold görüntüsünü kesiştirip dolu piksel sayısını bul
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            total = cv2.countNonZero(mask)


            # Sadece belirli bir piksel sayısının üzerindeki konturları değerlendir
            if total >= 1500: # Eşik değer, kaleme göre ayarlanabilir
                if bubbled is None or total > bubbled[0]:
                    bubbled = (total, j)

        # Doğru cevabı kontrol et
        q_num = start_q + q
        k = answer_key.get(q_num, -1)
        color = (0, 0, 255)  # Yanlışsa Kırmızı
        if bubbled is None:
            color = (255, 0, 0)  # Hiçbir şık işaretlenmemişse mavi

        elif k == bubbled[1]:
            color = (0, 255, 0)  # Doğruysa Yeşil
            correct_count += 1

        # İşaretlenen şıkkı çiz
        if bubbled is not None:
            cv2.drawContours(image_roi, [cnts_row[bubbled[1]]], -1, color, 3)

    return correct_count, image_roi


# 1. Görüntüyü yükle
# Kendi dosya yolunu buraya yaz
image_path = "C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta23\\bos.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Görüntü bulunamadı!")
    exit()

# Orijinal görüntünün boyutlarını al
h, w = image.shape[:2]

# 2. Görüntüyü yapısal sütunlara böl (Soru 1-10 ve Soru 11-20 alanları)
# Bu oranlar senin gönderdiğin formun yapısına göre yaklaşık olarak ayarlanmıştır.
col1_roi = image[0:h, int(w*0.25):int(w*0.62)]  # Orta sütun (Sorular 1-10)
col2_roi = image[0:h, int(w*0.62):w]           # Sağ sütun (Sorular 11-20)


# 3. Sütunları işle
correct_1_10, result_col1 = process_omr_column(col1_roi, ANSWER_KEY, start_q=1)
correct_11_20, result_col2 = process_omr_column(
    col2_roi, ANSWER_KEY, start_q=11)

# 4. Sonuçları hesapla ve ekrana yazdır
total_correct = correct_1_10 + correct_11_20
score = (total_correct / 20.0) * 100

print(f"[BİLGİ] Toplam Doğru: {total_correct}/20")
print(f"[BİLGİ] Sınav Puanı: {score:.2f}%")

cv2.putText(image, f"Skor: {score:.2f}%", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)

# Görüntüleri ekranda göster (Ekrana sığması için yeniden boyutlandırıyoruz)
image_resized = imutils.resize(image, height=700)
cv2.imshow("Optik Okuyucu Sonucu", image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
