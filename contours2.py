import numpy as np
import cv2

# Look for Contours using hsv space

img = cv2.imread('./images/perspective-06-small.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
#blur = cv2.medianBlur(v,5)
blur = cv2.GaussianBlur(v, (5,5),0)
_, thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the index of the largest contour
areas = []
for c in contours:
	areas.append(cv2.contourArea(c))
max_index = np.argmax(areas)
largest_area = contours[max_index]

# get bounding rectangle
x,y,w,h = cv2.boundingRect(largest_area)
cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255),2)

cv2.imshow('debug', thresh)
cv2.imshow('original', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
