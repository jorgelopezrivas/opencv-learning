import cv2
import numpy as np

# Based on http://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
img = cv2.imread('./images/perspective-11-small.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
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
 
# show the contour (outline) of the piece of paper
print "STEP 2: Find contours of paper"
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", img)

cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
