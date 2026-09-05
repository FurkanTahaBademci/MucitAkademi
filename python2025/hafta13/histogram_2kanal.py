import cv2
import matplotlib.pyplot as plt

image = cv2.imread('klon.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title('Grayscale Histogram')
plt.show()