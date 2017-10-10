import cv2
import numpy as np


img = cv2.imread('./images/perspective-01-small.jpg', 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, th2 = cv2.threshold(cl1,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('clahe', cl1)
cv2.imshow('thresh original', th1)
cv2.imshow('thresh clahe', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
