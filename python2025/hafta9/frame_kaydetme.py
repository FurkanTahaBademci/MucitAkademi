import cv2


count = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Video açılamadı. Dosya yolu veya codec kontrol edin.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        # Video bitti veya frame okunamadı
        break

    cv2.imshow('Video Frame', frame)

    # 30 ms bekle; eğer 'q' tuşuna basılmışsa döngüden çık
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    if cv2.waitKey(30) & 0xFF == ord('s'):
        cv2.imwrite(f"C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta9\\kamera_kayit_{count}.jpg", frame)
        count += 1

cap.release()
cv2.destroyAllWindows()