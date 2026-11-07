import cv2
import numpy as np


image = cv2.imread(
    "C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta9\\klon.jpg")

canvas = np.zeros((426, 640, 3), dtype="uint8")


image1 = cv2.resize(image, (640, 426))
image2 = cv2.resize(canvas, (640, 426))

cv2.addWeighted(image1, 0.9, image2, 0.1, 0, dst=image1)


cv2.imshow("orjınal", image)
cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.waitKey(0)

cv2.destroyAllWindows()