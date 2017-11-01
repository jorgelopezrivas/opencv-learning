import cv2
import numpy as np
from math import sqrt

def distance(a, b):
	dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
	return dist
	
def getRectangleDimentions(box, angle):
	#receives two values, return height = largest number and width = smallest
	side_a = distance(box[0], box[1])
	side_b = distance(box[1], box[2])
	
	#calculate w and h
	if side_a > side_b:
		h = side_a
		w = side_b
	else:
		h = side_b
		w = side_a
		
	#calculate angle
	if side_a < side_b:
		ret_angle = 90.00 + angle
	else:
		ret_angle = angle
	
	return w,h, ret_angle
	
def fixRotation(img):
	fp_contour = get_fingerprint_contour(img)
	rect = cv2.minAreaRect(fp_contour)

	box = cv2.boxPoints(rect)
	box = np.int0(box)
	w,h,angle = getRectangleDimentions(box, rect[2])
	
	
	#cv2.drawContours(img,[box],0,(0,0,255),2)
	#cv2.imshow('rect', img)
	
	rotations = []
	rows,cols = img.shape[0], img.shape[1]
	M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
	rotations.append(cv2.warpAffine(img,M,(cols,rows)))
	M = cv2.getRotationMatrix2D((cols/2,rows/2),angle+180,1)
	rotations.append(cv2.warpAffine(img,M,(cols,rows)))
	return rotations
			
def get_fingerprint_contour(img):
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (36,36))
	
	#Use the inverse image
	img = cv2.bitwise_not(img)
	# Otsu-s is the best for TH because of bimodal histogram
	ret,img = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	#cv2.imshow('th', img)
	# make fingerprint bigger so we can generate only one contour (retr external)
	img = cv2.dilate(img, kernel, iterations = 1)
	_, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#cv2.imshow('dilate', img)
	# Find the index of the largest contour
	areas = []
	for c in contours:
		areas.append(cv2.contourArea(c))
	max_index = np.argmax(areas)
	largest_area = contours[max_index]	

	return largest_area
	
def crop_monAreaRect():
	# rotate bounding box
	#rect0 = (rect[0], rect[1], 0.0)
	#box = cv2.boxPoints(rect)
	#pts = np.int0(cv2.transform(np.array([box]), M))[0]    
	#pts[pts < 0] = 0

	# crop
	#img_crop = img_rot[pts[1][1]:pts[0][1], pts[1][0]:pts[2][0]]
	img_crop = img_rot
	return img_crop

########################################################################
# MAIN    
########################################################################

#https://www.packtpub.com/books/content/fingerprint-detection-using-opencv-3


original = cv2.imread('images/01_117deg.bmp',1)
img = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
rotated = fixRotation(img)


cv2.imshow('img',original)
cv2.imshow('rotated 1', rotated[0])
cv2.imshow('rotated 2', rotated[1])
cv2.waitKey(0)
cv2.destroyAllWindows()


