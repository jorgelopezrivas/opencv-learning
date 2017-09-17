import numpy as np
import cv2

# Look for Contours

# Use YUV space
img = cv2.imread('./images/perspective-01-small.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)
#equ = cv2.equalizeHist(gray)
_, thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


largest_area = 0
largest_area_index = 0
i = 0;
for c in contours:
	area = cv2.contourArea(c)
	if area > largest_area:
		largest_area = area
		largest_area_index = i
	i += 1
	
cv2.drawContours(img, contours, largest_area_index, (0,255,0), 3)
cv2.imshow('thresh', thresh)
cv2.imshow('original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
