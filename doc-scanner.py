import numpy as np
import cv2

# Document Scanner:
# Draws contour around document.
# Documents must be flat over a surface


cap = cv2.VideoCapture(0)

while(True):
	ret, original = cap.read()
	gray = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
	#gray = cv2.GaussianBlur(gray, (5, 5), 0)
	#_, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	edged = cv2.Canny(gray, 100, 200)
	(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
	
	# loop over the contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	 
		# if our approximated contour has four points, then we
		# can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			break
	
	if screenCnt.any():
		cv2.drawContours(original, [screenCnt], -1, (0, 255, 0), 2)
	cv2.imshow('debug', edged)
	cv2.imshow('original', original)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



cap.release()
cv2.destroyAllWindows()
