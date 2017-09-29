''' Write a computer program capable of reducing the number of intensity 
levels in an image from 256 to 2, in integer powers of 2. The desired 
number of intensity levels needs to be a variable input to your program.'''

from matplotlib import pyplot as plt
import numpy as np
import cv2
x = 8


img1 = cv2.imread('./images/standard_images/lena_gray_512.tif',cv2.IMREAD_GRAYSCALE)
img2 = img1 / x * x
#hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
#plt.plot(hist1)
#plt.xlim([0,256])
#plt.show()

#hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
#plt.plot(hist2)
#plt.xlim([0,256])
#plt.show()

cv2.imshow('frame', img1)
cv2.imshow('frame2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

