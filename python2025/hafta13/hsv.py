import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)

cv2.namedWindow('Trackbars')

# Trackbar'ları oluştur
cv2.createTrackbar('Lower H', 'Trackbars', 0, 180, nothing)
cv2.createTrackbar('Lower S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Lower V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Upper H', 'Trackbars', 180, 180, nothing)
cv2.createTrackbar('Upper S', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('Upper V', 'Trackbars', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Orijinal frame'i kopyala
    display_frame = frame.copy()
    
    # BGR'den HSV'ye dönüştür
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar değerlerini al
    lower_h = cv2.getTrackbarPos('Lower H', 'Trackbars')
    lower_s = cv2.getTrackbarPos('Lower S', 'Trackbars')
    lower_v = cv2.getTrackbarPos('Lower V', 'Trackbars')
    upper_h = cv2.getTrackbarPos('Upper H', 'Trackbars')
    upper_s = cv2.getTrackbarPos('Upper S', 'Trackbars')
    upper_v = cv2.getTrackbarPos('Upper V', 'Trackbars')

    # Alt ve üst sınırları oluştur
    lower_bound = np.array([lower_h, lower_s, lower_v])
    upper_bound = np.array([upper_h, upper_s, upper_v])
    
    # Maskeyi oluştur
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    
    # Morfolojik işlemler - gürültüyü temizle
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Bulunan cisimleri orijinal görüntüde işaretle
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Küçük gürültüleri filtrele
        if area > 100:
            # Konturun etrafına çember çiz
            (x, y), radius = cv2.minEnclosingCircle(contour)
            x, y, radius = int(x), int(y), int(radius)
            cv2.circle(display_frame, (x, y), radius, (0, 255, 0), 2)
            
            # Konturun etrafına dikdörtgen çiz
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(display_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Merkez noktasını işaretle
            cv2.circle(display_frame, (x + w // 2, y + h // 2), 5, (0, 0, 255), -1)

    # Sonucu göster
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame (İşaretlenmiş)', display_frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Filtered Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()