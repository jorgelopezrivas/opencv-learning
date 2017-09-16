#!/usr/bin/env python
 
import numpy as np
import cv2
 
img_fn = './images/04.jpg'
img = cv2.imread(img_fn)
ksize = 11
theta = 0
kern = cv2.getGaborKernel((ksize, ksize), 2.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
cv2.imshow('result', fimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
