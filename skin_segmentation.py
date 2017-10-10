import cv2
import numpy as np

# https://stackoverflow.com/questions/14752006/computer-vision-masking-a-human-hand/14756351#14756351
# 
cap = cv2.VideoCapture(0)

#Kernels
kernel = np.ones((5,5), np.uint8)	#Square
elliptical_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

def removeLumaYCrCb(img):
	img[2,:,:] = 0
	return img

while(True):
	ret, originalImg = cap.read()
	resultImg = cv2.cvtColor(originalImg,cv2.COLOR_BGR2YCR_CB) #BGR2YCrCb
	resultImg = removeLumaYCrCb(resultImg)
	resultImg = cv2.GaussianBlur(resultImg, (7, 7), 0)
	# Face Segmentation Using skin-color map in videophone applications by chai and ngan:
	skin_min = np.array((0, 133, 77))
	skin_max = np.array((255, 173, 127))
	skin_ycrcb = cv2.inRange(resultImg, skin_min, skin_max)
	opening = cv2.morphologyEx(skin_ycrcb, cv2.MORPH_OPEN, elliptical_kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, elliptical_kernel)

	_, contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for i, c in enumerate(contours):
		area = cv2.contourArea(c)
		if area > 1000:
			cv2.drawContours(originalImg, contours, i, (255, 0, 0), 3)  
	cv2.putText(originalImg, "Koala contactless", (10,40), cv2.FONT_HERSHEY_SIMPLEX,1,255)
	cv2.imshow('frame', originalImg)
	#cv2.imshow('Y',y)
	#cv2.imshow('U',u)
	#cv2.imshow('V',v)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

