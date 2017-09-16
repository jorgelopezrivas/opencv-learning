import cv2
import numpy as np
from matplotlib import pyplot as plt
import basicops as bo

image = bo.getBlankImage(300,300, (255,0,0))
cv2.imshow('original', image)

#BGR Color:
color = (0, 255, 0)
# half-half
image[:,150] = color
cv2.imshow('half', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
