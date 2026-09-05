import numpy as np
import cv2
import imutils
from imutils.perspective import four_point_transform
from imutils import contours


ANSWER_KEY = {0: 4, 1: 4, 2: 4, 3: 4, 4: 4}

image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta22\\cevap20x5_v2.png")

alan1 = image[10:1200, 10:370]
w, h = alan1.shape[:2]
# cv2.imshow("alan1", cv2.resize(alan1, (h//2, w//2)))
# cv2.waitKey(0)

gray = cv2.cvtColor(alan1, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(alan1, cnts[0], -1, (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)

cnts = imutils.grab_contours(cnts)

questionCnts = []

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
        questionCnts.append(c)




questionCnts = contours.sort_contours(questionCnts,
	method="top-to-bottom")[0]
correct = 0



for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
    cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
    bubbled = None

    for (j, c) in enumerate(cnts):
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)

        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)

        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)


    color = (0, 0, 255)
    k = ANSWER_KEY[q]

    if k == bubbled[1]:
        color = (0, 255, 0)
        correct += 1

    cv2.drawContours(image, [cnts[k]], -1, color, 3)
    cv2.imshow("Exam", image)



score = (correct / len(ANSWER_KEY)) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(image, "{:.2f}%".format(score), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", image)
cv2.waitKey(0)