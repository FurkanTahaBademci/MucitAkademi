import cv2

image = cv2.imread(
    "C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta7\\klon.jpg")

print(image)

image_crop = image[164:233, 400:460]

print(image_crop.shape)


resized_image = cv2.resize(image_crop, (500, 500))

cv2.imshow("Image", image)
cv2.imshow("Cropped Image", image_crop)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
