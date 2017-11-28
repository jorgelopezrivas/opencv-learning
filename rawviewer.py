# open raw image
# https://stackoverflow.com/questions/18682830/opencv-python-display-raw-image

import numpy as np
import cv2

fd = open('./images/Huellas/test/in.raw', 'rb')
rows = 376
cols = 256
f = np.fromfile(fd, dtype=np.uint8,count=rows*cols)
im = f.reshape((rows, cols)) #notice row, column format
fd.close()

cv2.imshow('raw', im)
cv2.waitKey()
cv2.destroyAllWindows()
