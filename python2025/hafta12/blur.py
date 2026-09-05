import cv2


image = cv2.imread('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta12\\median.jpg')


median_blurred_image = cv2.medianBlur(image, 21)
blurred_image = cv2.blur(image, (21, 21))
gaussian_blurred_image = cv2.GaussianBlur(image, (21, 21), 0)
bilaterdal_blurred_image = cv2.bilateralFilter(image, 30, 75, 75)




cv2.imshow('Original Image', image)
cv2.imshow('Averaging Blur Image', blurred_image)
cv2.imshow('Median Blur Image', median_blurred_image)
cv2.imshow('Gaussian Blur Image', gaussian_blurred_image)
cv2.imshow('Bilateral Blur Image', bilaterdal_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()