import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python2026\\hafta11\\klon.jpg')

color = ('b','g','r')

for i,col in enumerate(color):

    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

cv2.imshow("Image", image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()