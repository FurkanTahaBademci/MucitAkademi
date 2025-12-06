import cv2


image = cv2.imread('3.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 30)
print(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)

cv2.imshow('Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()