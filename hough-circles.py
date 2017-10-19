import cv2
import numpy as np

img = cv2.imread('./images/monedas.jpg', 1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(gray,(21,21),0)

cv2.imshow('blur', blur)
#Python: cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]])  circles
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=35, param2=75, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
print circles.shape
print circles
for i in circles[0,:]:
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
cv2.imshow('Original', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
