import cv2
import numpy as np


canvas1 = 255 * np.ones((500, 500, 3), dtype="uint8")
canvas2 = 255 * np.ones((500, 500, 3), dtype="uint8")


cv2.line(canvas1, (50, 50), (100, 450), (255, 0, 0), 5)
cv2.line(canvas2, (50, 100), (450, 100), (0, 255, 0), 5)


cv2.addWeighted(canvas1, 0.5, canvas2, 0.5, 0, canvas1)


cv2.imshow("Drawing canvas1", canvas1)
cv2.imshow("Drawing canvas2", canvas2)
cv2.waitKey(0)
