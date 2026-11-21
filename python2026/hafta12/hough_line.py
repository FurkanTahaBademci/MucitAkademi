
import cv2
import numpy as np

image = cv2.imread(r'C:\Users\furkan\Desktop\MucitAkademi\python2026\hafta12\line.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


roi = gray[55:310, 60:340]

cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges = cv2.Canny(roi, 50, 150)     #kenarlar belirginleşti


cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

line = cv2.HoughLinesP(
    edges,
    1,
    np.pi / 180,
    threshold=50,
    minLineLength=80,
    maxLineGap=10
)

if line is not None:
    for x1, y1, x2, y2 in line.reshape(-1, 4):


        x1 += 60
        x2 += 60
        y1 += 55
        y2 += 55

        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Hough Line Transform', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
