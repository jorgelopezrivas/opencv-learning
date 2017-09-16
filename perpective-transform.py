# perspective-transform.py
# Perspective Transform for documents

import numpy as np
import cv2

def getPointsDistance(pt1, pt2):
	res = np.sqrt(((pt1[0] - pt2[0]) ** 2) + ((pt1[1] - pt2[1]) ** 2))
	return res

# Esquinas:
# 1. Top Left		20,368
# 2. Top Right  	277,184
# 3. Bottom Right 	425,203
# 4. Bottom Left	216,477

img = cv2.imread('./images/perspective-05-small.jpg',1)
imgCorners = np.float32([(20,368), (277,184),(425,203),(216,477)])
for c in imgCorners:
	cv2.circle(img, (c[0],c[1]), 3, (0,0,255), -1)

# Get Max Height
height1 = getPointsDistance(imgCorners[0], imgCorners[3]) 
height2 = getPointsDistance(imgCorners[1], imgCorners[2])
maxHeight = max(int(height1), int(height2))

# Get Max Width (based on longest diagonal)
width1 = getPointsDistance(imgCorners[0], imgCorners[2])
width2 = getPointsDistance(imgCorners[1], imgCorners[3])
maxWidth = max(int(width1), int(width2))

# Transform Perspective
resCorners = np.float32([(0,0), (maxWidth,0), (maxWidth,maxHeight), (0,maxHeight)])
M = cv2.getPerspectiveTransform(imgCorners, resCorners)
res = cv2.warpPerspective(img, M, (maxWidth,maxHeight))

cv2.imshow('original', img)
cv2.imshow('resultado', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
