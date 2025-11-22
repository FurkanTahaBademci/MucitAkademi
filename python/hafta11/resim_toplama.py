import cv2
import numpy as np

image1 = cv2.imread(
    "C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta11\\resim1.jpg")


canvas = 0 * np.ones((600, 400, 3), dtype="uint8")


image1 = cv2.resize(image1, (600, 400))
image2 = cv2.resize(canvas, (600, 400))

cv2.addWeighted(image1, 0.6, image2, 0.4, 0, dst=image1)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.waitKey(0)

cv2.destroyAllWindows()