import cv2
import numpy as np

canvas =  np.ones((500, 500), dtype="uint8") * 255

cv2.line(canvas, (0, 0), (500, 500), 0, 10)
cv2.line (canvas, (50, 50), (150, 500), 0, 1)

eroded = cv2.erode(canvas, np.ones((5,5), np.uint8), iterations=1)
dilated = cv2.dilate(canvas, np.ones((5,5), np.uint8), iterations=1)

cv2.imshow("Canvas", canvas)
cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)

cv2.destroyAllWindows()



