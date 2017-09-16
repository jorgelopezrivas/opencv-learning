import cv2
import numpy as np


def nothing(x):
    pass
    
def getOdd(x):
	if x <= 0:
		return 1
	elif x % 2 == 0:
		return x+1
	else:
		return x
		
def getOddBlockSize(x):
	if x < 3:
		return 3
	else:
		return getOdd(x)
	
		
#read source image
img = cv2.imread('./images/file.png', 0)
cv2.namedWindow('Image')

# create trackbar for param change
cv2.createTrackbar('Blur','Image', 0, 30, nothing)
cv2.createTrackbar('BlockSize', 'Image', 0, 41, nothing)

blur = 1
blockSize = 3
kernel = np.ones((5,5),np.float32)/25

while(1):
	# Apply blur for noise reduction
	img_blur = cv2.medianBlur(img, getOdd(blur))
	#threshold
	img_th = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, getOddBlockSize(blockSize), 1)	
	#Filter
	img_flt = cv2.filter2D(img_th,-1,kernel)

	cv2.imshow("Image", img_flt)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	blur = cv2.getTrackbarPos('Blur', 'Image')
	blockSize = cv2.getTrackbarPos('BlockSize', 'Image')


cv2.destroyAllWindows()
