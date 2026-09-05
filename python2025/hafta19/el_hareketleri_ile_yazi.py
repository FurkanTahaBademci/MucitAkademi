import cv2
import numpy as np
from collections import deque


# Farklı renkler için ayrı deque'ler
noktalar = {
    "kirmizi": deque(maxlen=500),
    "yesil": deque(maxlen=500),
    "mavi": deque(maxlen=500),
    "sari": deque(maxlen=500)
}

# Aktif renk
aktif_renk = "kirmizi"


def araliklari_belirle(x, y):
    if 10 < x < 110 and 10 < y < 80:
        return "sil"
    elif 130 < x < 230 and 10 < y < 80:
        return "kirmizi"
    elif 250 < x < 350 and 10 < y < 80:
        return "yesil"
    elif 370 < x < 470 and 10 < y < 80:
        return "mavi"
    elif 490 < x < 590 and 10 < y < 80:
        return "sari"
    else:
        return "bos"


cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    height, width, _ = frame.shape

    # Orijinal frame'i kopyala
    display_frame = frame.copy()

    # BGR'den HSV'ye dönüştür
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Sarı renk aralığını tanımla
    # Alt ve üst sınırları oluştur
    lower_bound = np.array([20, 100, 100])
    upper_bound = np.array([30, 255, 255])

    # Maskeyi oluştur
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # Morfolojik işlemler - gürültüyü temizle
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Konturları bul
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Kontrol butonları çiz
    cv2.rectangle(display_frame, (10, 10), (110, 80), (50, 50, 50), 3)
    cv2.putText(display_frame, "SIL", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    cv2.rectangle(display_frame, (130, 10), (230, 80), (0, 0, 255), -1)
    cv2.putText(display_frame, "KIRMIZI", (135, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.rectangle(display_frame, (250, 10), (350, 80), (0, 255, 0), -1)
    cv2.putText(display_frame, "YESIL", (260, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv2.rectangle(display_frame, (370, 10), (470, 80), (255, 0, 0), -1)
    cv2.putText(display_frame, "MAVI", (385, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv2.rectangle(display_frame, (490, 10), (590, 80), (25, 215, 250), -1)
    cv2.putText(display_frame, "SARI", (510, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Tüm renk deque'lerini çiz
    renk_kodlari = {
        "kirmizi": (0, 0, 255),
        "yesil": (0, 255, 0),
        "mavi": (255, 0, 0),
        "sari": (0, 255, 255)
    }

    for renk_adi, nokta_listesi in noktalar.items():
        if len(nokta_listesi) > 1:
            for i in range(1, len(nokta_listesi)):
                if nokta_listesi[i - 1] is None or nokta_listesi[i] is None:
                    continue
                # noktalar arası uzaklık çok fazla ise çizme
                dist = np.linalg.norm(
                    np.array(nokta_listesi[i]) - np.array(nokta_listesi[i - 1]))
                if dist < 50:
                    cv2.line(display_frame, nokta_listesi[i - 1],
                            nokta_listesi[i], renk_kodlari[renk_adi], 5)
        
    # Bulunan cisimleri orijinal görüntüde işaretle
    for contour in contours:
        area = cv2.contourArea(contour)

        # Küçük gürültüleri filtrele
        if area > 250:
            # Konturun etrafına çember çiz
            (x, y), radius = cv2.minEnclosingCircle(contour)
            x, y, radius = int(x), int(y), int(radius)
            cv2.circle(display_frame, (x, y), radius, (0, 255, 0), 2)

            # Konturun etrafına dikdörtgen çiz
            x, y, w, h = cv2.boundingRect(contour)
            # cv2.rectangle(display_frame, (x, y),
            #               (x + w, y + h), (255, 0, 0), 2)
            
            merkez_x = x + w // 2
            merkez_y = y + h // 2
            renk = araliklari_belirle(merkez_x, merkez_y)
            
            if renk == "sil":
                # Tüm deque'leri temizle
                for deque_renk in noktalar:
                    noktalar[deque_renk].clear()
                print("Tüm çizimler silindi")
            elif renk in noktalar:
                # Aktif rengi değiştir
                aktif_renk = renk
                print(f"Aktif renk: {renk}")
            elif renk == "bos":
                # Aktif renge nokta ekle
                noktalar[aktif_renk].append((merkez_x, merkez_y))
                
            # Merkez noktasını işaretle
            cv2.circle(display_frame, (merkez_x, merkez_y),
                       5, (0, 0, 255), -1)

    cv2.imshow('El Hareketleri ile Yazi', display_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
