import cv2

image = cv2.imread(
    "C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta7\\klon.jpg")


image_crop = image[164:233, 400:460]

cv2.imwrite(
    "C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta7\\klon_cropped.jpg",
    image_crop)
