import cv2
import numpy as np

# Boş bir beyaz tuval oluştur
canvas = 255 * np.ones((750, 750, 3), dtype="uint8")

cv2.namedWindow("Drawing Canvas")
cv2.imshow("Drawing Canvas", canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()