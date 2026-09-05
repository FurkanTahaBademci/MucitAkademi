import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Trackbars')

# Trackbar'ları oluştur
cv2.createTrackbar('Lower H', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Lower S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Lower V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Upper H', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Upper S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Upper V', 'Trackbars', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

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

    # Sonucu göster
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()