import cv2
import matplotlib.pyplot as plt

image = cv2.imread(
    'C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta16\\klon.jpg')

w, h = image.shape[1], image.shape[0]

resized_image_half = cv2.resize(image, (w // 2, h // 2))
resized_image_double = cv2.resize(image, (w * 2, h * 2))


print(f'Original Image Size: {image.shape[1]}x{image.shape[0]}')
print(
    f'Resized Image Half Size: {resized_image_half.shape[1]}x{resized_image_half.shape[0]}')
print(
    f'Resized Image Double Size: {resized_image_double.shape[1]}x{resized_image_double.shape[0]}')


final_half = cv2.resize(resized_image_half, (640, 426))
final_double = cv2.resize(resized_image_double, (640, 426))
final_orjinal = cv2.resize(image, (640, 426))

cv2.imshow('Original Image', final_orjinal)
cv2.imshow('Resized Image Half', final_half)
cv2.imshow('Resized Image Double', final_double)


color = ('b', 'g', 'r')

# Histogram for Half-sized image
plt.figure(figsize=(10, 6))
for i, col in enumerate(color):
    histr1 = cv2.calcHist([final_half], [i], None, [256], [0, 256])
    plt.plot(histr1, color=col, label=f'{col.upper()} channel')
    plt.xlim([0, 256])

plt.title('Histogram - Half Sized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()

# Histogram for Double-sized image
plt.figure(figsize=(10, 6))
for i, col in enumerate(color):
    histr2 = cv2.calcHist([final_double], [i], None, [256], [0, 256])
    plt.plot(histr2, color=col, label=f'{col.upper()} channel')
    plt.xlim([0, 256])

plt.title('Histogram - Double Sized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()

# Histogram for Original image
plt.figure(figsize=(10, 6))
for i, col in enumerate(color):
    histr3 = cv2.calcHist([final_orjinal], [i], None, [256], [0, 256])
    plt.plot(histr3, color=col, label=f'{col.upper()} channel')
    plt.xlim([0, 256])

plt.title('Histogram - Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
