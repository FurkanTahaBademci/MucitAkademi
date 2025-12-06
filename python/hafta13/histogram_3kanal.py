import cv2
import matplotlib.pyplot as plt

image = cv2.imread('klon.jpg')

color = ('b','g','r')

for i,col in enumerate(color):

    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()