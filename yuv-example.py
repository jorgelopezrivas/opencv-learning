import cv2
import numpy as np
from matplotlib import pyplot as plt

# YUV equalization
# based on
# https://stackoverflow.com/questions/18452438/how-can-i-remove-drastic-brightness-variations-in-a-video/18453032#18453032
# http://answers.opencv.org/question/117045/how-to-remove-bad-lighting-conditions-or-shadow-effects-in-images-using-opencv-for-processing-face-images/


img = cv2.imread('./images/perspective-05-small.jpg',1)
yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
y,u,v = cv2.split(yuv)

cv2.imshow('original', img)
cv2.imshow('yuv', yuv)
cv2.imshow('y', y)
cv2.imshow('u', u)
cv2.imshow('v', v)
cv2.waitKey(0)
cv2.destroyAllWindows()

