import cv2

cap = cv2.VideoCapture('/home/furkan/MucitAkademi/python2026/hafta8/antalya.mp4')

if not cap.isOpened():
    print("Video açilamadi. Dosya yolu veya codec kontrol edin.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
            # Video bitti veya frame okunamadı
            break
    cv2.imshow('Video Frame', frame)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()