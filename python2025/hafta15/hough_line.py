import cv2
import numpy as np

image = cv2.imread('line.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



line = cv2.HoughLinesP(
    gray,
    2,
    np.pi / 180,
    threshold=950,
    minLineLength=60,
    maxLineGap=250
)

# blur : girdi görüntüsü
# 1 : rho çözünürlüğü (piksel cinsinden)
# np.pi / 180 : theta çözünürlüğü (radyan cinsinden
# threshold=100 : minimum oy sayısı
# minLineLength=100 : minimum çizgi uzunluğu
# maxLineGap=10 : maksimum boşluk uzunluğu

for x1, y1, x2, y2 in line[:, 0]:
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
cv2.imshow('Hough Line Transform', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
