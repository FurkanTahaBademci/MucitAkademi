import cv2
import numpy as np

canvas =  np.ones((500, 500), dtype="uint8") * 255

cv2.line(canvas, (0, 0), (500, 500), 0, 10)
cv2.line (canvas, (50, 50), (150, 500), 0, 1)

eroded = cv2.erode(canvas, (15,15), iterations=10)
dilated = cv2.dilate(canvas, (15,15), iterations=20)

cv2.imshow("Canvas", canvas)
cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)

cv2.destroyAllWindows()



