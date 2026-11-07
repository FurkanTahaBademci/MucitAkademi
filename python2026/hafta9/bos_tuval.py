import cv2
import numpy as np

canvas = np.zeros((500, 500, 3), dtype=np.uint8)

canvas[100:200, 100:200] = (0, 255, 0)
canvas[200:300, 200:300] = (0, 0, 255)
canvas[300:400, 100:200] = (255, 100, 0)  # BLUE GREEN RED


cv2.imshow("Empty Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()