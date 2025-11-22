import cv2


image = cv2.imread('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta11\\klon.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_MASK)

cv2.imshow('Gray Image', gray)
cv2.imshow('Binary Image', binary)

cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()