import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass


cv2.namedWindow('control')
kernel = np.ones((20,20), np.uint8)

# Hue
lh = 106
hh = 158
cv2.createTrackbar('lh','control',0,255,nothing)
cv2.setTrackbarPos('lh', 'control', lh)
cv2.createTrackbar('hh','control',0,255,nothing)
cv2.setTrackbarPos('hh', 'control', hh)

#Saturation 
ls = 83
hs = 168
cv2.createTrackbar('ls','control',0,255,nothing)
cv2.setTrackbarPos('ls', 'control', ls)
cv2.createTrackbar('hs','control',0,255,nothing)
cv2.setTrackbarPos('hs', 'control', hs)

lv = 0
hv = 72
cv2.createTrackbar('lv','control',0,255,nothing)
cv2.setTrackbarPos('lv', 'control', lv)
cv2.createTrackbar('hv','control',0,255,nothing)
cv2.setTrackbarPos('hv', 'control', hv)

cap = cv2.VideoCapture(0)
while(1):
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# get all positions
	lowH=cv2.getTrackbarPos('lh', 'control')
	highH=cv2.getTrackbarPos('hh', 'control')
	lowS=cv2.getTrackbarPos('ls', 'control')
	highS=cv2.getTrackbarPos('hs', 'control')
	lowV=cv2.getTrackbarPos('lv', 'control')
	highV=cv2.getTrackbarPos('hv', 'control')
	lower = np.array([lowH,lowS,lowV])
	upper = np.array([highH,highS,highV])
	th = cv2.inRange(hsv, lower, upper)
	opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)
	
	#calculate moments
	#contours, hierarchy = cv2.findContours(closing, 1, 2)
	res, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	if contours:
		cnt = contours[0]
		M = cv2.moments(cnt)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		cv2.circle(frame, (cX, cY),10, (0,0,255), 2)
	#cv2.imshow('video',frame)
	cv2.imshow('detector', closing)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
		
# Release everything if job is finished
cap.release()

cv2.destroyAllWindows()

