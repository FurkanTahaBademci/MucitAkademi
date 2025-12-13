import cv2


image = cv2.imread('conturs2.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

thresh = cv2.blur(thresh, (5,5),0)
erode = cv2.erode(thresh, (11,11), iterations=5)

# Find contours
contours, _ = cv2.findContours(
    erode , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f'Number of contours found: {len(contours)}')
print('Contours:', contours)


for cnt in contours:
    #area hesapla
    area = cv2.contourArea(cnt)
    if area > 300:
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()