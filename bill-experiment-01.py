#bill_experiment1.py

import cv2
import numpy as np
from matplotlib import pyplot as plt



srcImg = cv2.imread('bills/200-f02.jpg', 1)
#srcImg = cv2.resize(srcImg, (0,0), fx=0.5, fy=0.5)
cv2.imshow('Imagen Original', srcImg)


# Blackhat = Input - Opening
kernel = np.ones((3,3), np.uint8)	#Square
blackhat = cv2.morphologyEx(srcImg, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', blackhat)

#closing = cv2.morphologyEx(blackhat, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('Closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
