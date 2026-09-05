import cv2


image1 = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta18\\image2.png")
image2 = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta18\\klon.jpg")


image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

weighted_sum = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

cv2.imshow("Weighted Sum", weighted_sum)
cv2.waitKey(0)
cv2.destroyAllWindows()