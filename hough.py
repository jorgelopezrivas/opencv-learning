import cv2
import numpy as np

#Hough Transform
# Feature extraction technique
# Line detection in an image 8straight lines(
# Opencv implements 3 kings of Hough Line Transforms
# 	- SHT: Standard Hough Transform
#	- MSHT: Multi Scale
#	- PPHT: Progressive Probabilistic


img = cv2.imread('./images/canny_input.jpg', 1)
cv2.imshow('Original', img)
img_lines = img;
edges = cv2.Canny(img, 50, 250, 3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for vector in lines:
	rho,theta = vector[0][:]
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
	
cv2.imshow('Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
