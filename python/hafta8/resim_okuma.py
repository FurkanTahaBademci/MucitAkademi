import cv2

# Load an image from file
image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta8\\klon.jpg")

print("Image shape:", image.shape)  # Print the dimensions of the image

image_2 = image[100:400, 200:500]  # Crop a region from the image
# Display the image in a window
cv2.imshow("resim", image)
cv2.imshow("resim_2", image_2)
cv2.waitKey(0)
