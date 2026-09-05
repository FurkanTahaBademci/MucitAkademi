import cv2
import numpy as np

# Load the image
image = cv2.imread('circle.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (9, 9), 2)


# dp  = Görüntü çözünürlüğü ile Hough Uzay çözünürlüğü arasındaki oranı belirtir.
# minDist = Algılanan daireler arasındaki minimum mesafe.
# param1 = Canny kenar algılama için kullanılan yüksek eşik değeri.
# param2 = Daire merkezlerinin algılanması için kullanılan eşik değeri.
# minRadius = Algılanacak dairelerin minimum yarıçapı.
# maxRadius = Algılanacak dairelerin maksimum yarıçapı.
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.1, minDist=80,
                           param1=120, param2=28, minRadius=8, maxRadius=150)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
        
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)