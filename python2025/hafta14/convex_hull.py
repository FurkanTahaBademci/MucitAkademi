import cv2

# Load the image
image = cv2.imread('convex_hul.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours and their convex hulls

for contour in contours:
    cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)
    
    hull = cv2.convexHull(contour)
    
    cv2.drawContours(image, [hull], -1, (0, 255, 0), 2)


cv2.imshow('Convex Hulls', image)
cv2.waitKey(0)
cv2.destroyAllWindows()