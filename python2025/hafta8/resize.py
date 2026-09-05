import cv2

# Load an image from file
image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta8\\klon.jpg")

image_resized = cv2.resize(image,(640//4, 480//4))

print("Image shape:", image.shape)  # Print the dimensions of the image

cv2.imshow("resim", image)
cv2.imshow("resim_2", image_resized)
cv2.waitKey(0)
