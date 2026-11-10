import cv2

image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta10\\klon.jpg")

blurred_image = cv2.GaussianBlur(image, (25, 5), 0)

cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()