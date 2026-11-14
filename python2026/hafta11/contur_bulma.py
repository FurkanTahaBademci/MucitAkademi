import cv2

image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta11\\3.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bitwise = cv2.bitwise_not(gray)

cv2.imshow("Inverted Gray", bitwise)

conturs, _ = cv2.findContours(bitwise, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in conturs:
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Contours", image)
    cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()
