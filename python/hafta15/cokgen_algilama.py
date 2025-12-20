import cv2

image = cv2.imread("C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta15\\cokgen.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)



contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



for contour in contours:

    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

    
    
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    
    if len(approx) == 3:
        cv2.putText(image, "Ücgen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)

    elif len(approx) == 4:
        cv2.putText(image, "Dörtgen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)
        
    elif len(approx) == 5:
        cv2.putText(image, "Beşgen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)
    elif len(approx) == 6:
        cv2.putText(image, "Altıgen", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)
    else:
        cv2.putText(image, "Daire", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        
cv2.imshow("Shapes", image)
cv2.waitKey(0)