
import cv2
import numpy as np

canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.circle(canvas, (250, 200), 100, (255, 200, 100), -1)

cv2.circle(canvas, (210, 180), 15, (255, 255, 255), -1)
cv2.circle(canvas, (290, 180), 15, (255, 255, 255), -1)

cv2.circle(canvas, (210, 180), 7, (0, 0, 0), -1)
cv2.circle(canvas, (290, 180), 7, (0, 0, 0), -1)

cv2.line(canvas, (250, 190), (240, 220), (0, 0, 255), 4)

cv2.line(canvas, (220, 250), (280, 250), (0, 0, 255), 5)

cv2.putText(canvas, "Deniz", (190, 400),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5,
            (255, 255, 255), 3)

cv2.imshow("My Avatar", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
