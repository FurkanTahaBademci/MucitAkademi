import cv2

image = cv2.imread('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta11\\klon.jpg')

cv2.imshow('Original Image', image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

cv2.imshow('HSV Image', hsv_image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('Lab Image', lab_image)
cv2.waitKey(0)
cv2.destroyAllWindows()