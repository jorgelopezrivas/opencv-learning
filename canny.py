import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass


img = cv2.imread('images/01.jpg', 0)
cv2.namedWindow('image')
cv2.createTrackbar('minVal', 'image', 0, 255, nothing)
cv2.createTrackbar('maxVal', 'image', 0, 255, nothing)

minVal = 0
maxVal = 0 

while(1):
	edges = cv2.Canny(img, minVal, maxVal)
	cv2.imshow('image', edges)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		
		break
	minVal = cv2.getTrackbarPos('minVal','image')
	maxVal = cv2.getTrackbarPos('maxVal','image')
	
	

cv2.destroyAllWindows()

