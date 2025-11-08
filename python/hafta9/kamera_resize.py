import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Video açılamadı. Dosya yolu veya codec kontrol edin.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        # Video bitti veya frame okunamadı
        break
    frame_resized = cv2.resize(frame, (640//2, 480//2))
    cv2.imshow('Video Frame', frame)
    cv2.imshow('Resized Frame', frame_resized)


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()