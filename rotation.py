import numpy as np
import cv2


img = cv2.imread('./images/standard_images/lena_gray_512.tif',cv2.IMREAD_GRAYSCALE)

#rotate 90 with np
img90 = np.rot90(img)

#rotate 45 with opencv
rows, cols = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
print M
img45 = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('frame1', img)
cv2.imshow('frame2', img90)
cv2.imshow('frame3', img45)

cv2.waitKey(0)
cv2.destroyAllWindows()
