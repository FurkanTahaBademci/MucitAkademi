import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta17\\somun.jpeg', cv2.IMREAD_GRAYSCALE)



img2 = img.copy()
template = cv2.imread('C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta17\\somun_tekli.jpeg', cv2.IMREAD_GRAYSCALE)


weight, height = template.shape


# All the 6 methods for comparison in a list
methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
            'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']



for meth in methods:
    img = img2.copy()
    method = getattr(cv2, meth)
 
    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + weight, top_left[1] + height)
 
    cv2.rectangle(img,top_left, bottom_right, 255, 2)
 

 
 
 
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
 
    plt.show()
    
    