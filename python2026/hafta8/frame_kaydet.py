import cv2

cap = cv2.VideoCapture(0)

sayac = 0

if not cap.isOpened():
    print("Video açılamadı. Dosya yolu veya codec kontrol edin.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        # Video bitti veya frame okunamadı
        break
    
    cv2.imshow('Video Frame', frame)
    


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    if cv2.waitKey(30) & 0xFF == ord('s'):
            print(f'frame kaydedildi, {sayac}')
            cv2.imwrite(
    f'/home/furkan/MucitAkademi/python2026/hafta8/frames/frame_{sayac}.jpg',
    frame)
            sayac = sayac +1  # sayac+=1            
cap.release()
cv2.destroyAllWindows()