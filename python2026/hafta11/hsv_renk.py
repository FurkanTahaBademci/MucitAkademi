import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar değerlerini al
    lower_h = 100
    lower_s = 100
    lower_v = 100
    upper_h = 255
    upper_s = 255
    upper_v = 255

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