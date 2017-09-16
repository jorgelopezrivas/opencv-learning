import cv2
import numpy as np
from matplotlib import pyplot as plt

def build_filters():
	filters = []
	#ksize = 31
	ksize = 31
	for theta in np.arange(0, np.pi, np.pi / 16):
		kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
		kern /= 1.5*kern.sum()
		filters.append(kern)
	return filters
 
def gabor_segment(img, filters):
	accum = np.zeros_like(img)
	for kern in filters:
		fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
		np.maximum(accum, fimg, accum)
	return accum

image = cv2.imread('./images/fap.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image = cv2.medianBlur(image, 27)
cv2.imshow('original',image)
img_segmented = gabor_segment(image, build_filters())
#cv2.imshow('gabor segmentation', img_segmented)

dst1 = cv2.adaptiveThreshold(img_segmented,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,15,1)
#cv2.imshow('threshold segmentation',dst1[::2,::2])
im2, contours, hierarchy = cv2.findContours(dst1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# remove small contours
print(len(contours))
for idx in range(len(contours)-1,-1,-1):
	if cv2.contourArea(contours[idx]) > 10:
		im3 = cv2.drawContours(image, contours, idx,(0,255,0), 1)
		#print(cv2.contourArea(contours[idx]))
				
cv2.imshow('xd',im3)
#cv2.imshow('final', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
