import cv2

# Load an image from file
image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta8\\klon.jpg")

print("Image shape:", image.shape)  # Print the dimensions of the image

image_2 = image[50:180, 200:350]  # Crop a region from the image

cv2.imwrite("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta8\\klon_cropped.jpg", image_2)
# Display the image in a window
cv2.imshow("resim", image)
cv2.imshow("resim_2", image_2)
cv2.waitKey(0)
