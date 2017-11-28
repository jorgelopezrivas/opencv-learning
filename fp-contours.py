import cv2
import numpy as np
from math import sqrt

def distance(a, b):
	dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
	return dist
	
def get_rectangle_dimentions(box, angle):
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
	
def fix_rotation(img):
	fp_contour = get_fingerprint_contour(img)
	rect = cv2.minAreaRect(fp_contour)
	box = cv2.boxPoints(rect)
	w,h,angle = get_rectangle_dimentions(box, rect[2])
	
	rotations = []
	rows,cols = img.shape[0], img.shape[1]
	
	# Obtener la imagen rotada 1/2
	M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
	img_rot = cv2.warpAffine(img,M,(cols,rows))
	img_crop = crop_min_area_rect(img_rot,box,M)
	rotations.append(img_crop)	
	
	# Obtener la imagen rotada 2/2
	M = cv2.getRotationMatrix2D((cols/2,rows/2),angle+180,1)
	img_rot = cv2.warpAffine(img,M,(cols,rows))
	img_crop = crop_min_area_rect(img_rot,box,M)
	rotations.append(img_crop)
	

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
	
def crop_min_area_rect(img,box,M):
	
	# rotate bounding box
	pts = np.int0(cv2.transform(np.array([box]), M))[0] 
	pts[pts < 0] = 0
	
	# get min and max values for x and y
	min_val = np.amin(pts, axis=0)
	max_val = np.amax(pts, axis=0)
	
	# crop
	img_crop = img[min_val[1]:max_val[1], min_val[0]:max_val[0]]
		
	return img_crop
	
def copy_image_centered(small, big):
	# paste small img in the center of big
	x_pos = (big.shape[1] / 2) - (small.shape[1] / 2)
	y_pos = (big.shape[0] / 2) - (small.shape[0] / 2)
	big[y_pos:y_pos + small.shape[0], x_pos:x_pos + small.shape[1]] = small
	return big
	
#def save_image(image):


########################################################################
# MAIN    
########################################################################

#https://www.packtpub.com/books/content/fingerprint-detection-using-opencv-3

original = cv2.imread('images/01_m145deg.bmp',1)
original = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

#create new blank image
work_img = np.zeros((original.shape[0]*2, original.shape[1]*2,3), np.uint8)
work_img[:] = (255,255,255)
work_img = cv2.cvtColor(work_img,cv2.COLOR_BGR2GRAY)

work_img = copy_image_centered(original, work_img)
rotated = fix_rotation(work_img)


cv2.imshow('original',original)
#cv2.imshow('big',work_img)
cv2.imshow('rotated 1', rotated[0])
cv2.imshow('rotated 2', rotated[1])
cv2.waitKey(0)
cv2.destroyAllWindows()


