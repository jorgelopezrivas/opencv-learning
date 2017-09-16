import cv2
import numpy as np
from matplotlib import pyplot as plt

srcImg = cv2.imread('images/file1.png', 0)
#srcImg = cv2.resize(srcImg, (0,0), fx=0.4, fy=0.4)
cv2.imshow('Imagen Original', srcImg)

#Kernels
kernel = np.ones((5,5), np.uint8)	#Square
elliptical_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50,50))

#create erosion
#np.ones(shape, dtype,order)

erosion = cv2.erode(srcImg, elliptical_kernel, iterations = 1)
cv2.imshow('Imagen con Erosion', erosion)

#create dilation
dilate = cv2.dilate(srcImg, elliptical_kernel, iterations = 1)
#cv2.imshow('Imagen dilatada', dilate)

#first erosion then dilation
both = cv2.dilate(erosion, elliptical_kernel, iterations = 1)
#cv2.imshow('Erosion dilatacion', both)

# erosion and dilation are mixed in the concept Opening
opening = cv2.morphologyEx(srcImg, cv2.MORPH_OPEN, elliptical_kernel)
cv2.imshow('Opening', opening)

#Closing is dilation and erosion
closing = cv2.morphologyEx(srcImg, cv2.MORPH_CLOSE, elliptical_kernel)
cv2.imshow('Closing', closing)

# Morphological gradient: diferencia entre dilatacion y erosion
gradient = cv2.morphologyEx(srcImg, cv2.MORPH_GRADIENT, elliptical_kernel)
#cv2.imshow('Gradient', gradient)

# TopHat = Input - Opening
tophat = cv2.morphologyEx(srcImg, cv2.MORPH_TOPHAT, elliptical_kernel)
cv2.imshow('tophat', tophat)

# Blackhat = Input - Opening
blackhat = cv2.morphologyEx(srcImg, cv2.MORPH_BLACKHAT, elliptical_kernel)
cv2.imshow('blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
