import cv2


image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta9\\klon.jpg")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("RGB Image", rgb_image)
cv2.imshow("LAB Image", lab)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()