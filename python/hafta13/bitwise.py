import cv2

image_1 = cv2.imread("1.png")
image_2 = cv2.imread("2.png")

result = cv2.bitwise_and(image_1, image_2)
result2 = cv2.bitwise_or(image_1, image_2)
result3 = cv2.bitwise_xor(image_1, image_2)
result4 = cv2.bitwise_not(image_1)


cv2.imshow("Image 1", image_1)
cv2.imshow("Image 2", image_2)
cv2.imshow("Bitwise AND", result)
cv2.imshow("Bitwise OR", result2)
cv2.imshow("Bitwise XOR", result3)
cv2.imshow("Bitwise NOT", result4)
cv2.waitKey(0)
cv2.destroyAllWindows()