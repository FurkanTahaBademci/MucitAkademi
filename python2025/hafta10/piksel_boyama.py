import cv2
import numpy as np

# Boş bir beyaz tuval oluştur
canvas = 255 * np.ones((750, 750, 3), dtype="uint8")
canvas[600:650,100:750] = [0, 255, 0]  # Pikseli yeşil yap
canvas[100:700,500:550] = [0, 0, 255]  # Pikseli kırmızı yap


cv2.namedWindow("Drawing Canvas")
cv2.imshow("Drawing Canvas", canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()