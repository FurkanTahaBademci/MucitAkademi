import cv2

a = 0
renk = (0, 255, 0)
sart = 0

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    frame_croped = frame[100:400, 200:400]

    cv2.rectangle(frame, (200, 100), (400, 400), renk, 2)
    cv2.imshow(' Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Q tuşuna basıldı")
        break

    if sart % 15 == 0:
        renk = (0, 255, 0)  # Değişen renk yeşil oldu

    if cv2.waitKey(1) & 0xFF == ord('s'):
        renk = (255, 0, 0)  # Değişen renk mavi oldu
        cv2.imwrite(
            f"C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta11\\kare_cropped_{a}.jpg", frame_croped)
        print("S tuşuna basıldı", f"kare_cropped_{a}.jpg kaydedildi.")
        a += 1

    sart += 1
    print(sart)

cap.release()
cv2.destroyAllWindows()
