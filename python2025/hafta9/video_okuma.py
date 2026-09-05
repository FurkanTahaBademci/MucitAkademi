import cv2

cap = cv2.VideoCapture('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta9\\antalya.mp4')

if not cap.isOpened():
    print("Video açılamadı. Dosya yolu veya codec kontrol edin.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        # Video bitti veya frame okunamadı
        break

    cv2.imshow('Video Frame', frame)

    # 30 ms bekle; eğer 'a' tuşuna basılmışsa döngüden çık
    if cv2.waitKey(30) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()