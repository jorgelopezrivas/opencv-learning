import numpy as np
import cv2
import glob

data = []
path = "./saved_frames/"
files = glob.glob(path + "*.jpg")
for myFile in files:
	image = cv2.imread(myFile,0)
	data.append(image)

# Hopefully align images
#alignMTB = cv2.createAlignMTB()
#alignMTB.process(data,data2)

median = np.median(np.array(data), axis=0).astype(np.uint8)
cv2.imwrite(path + "median.jpeg", median)
cv2.imshow('Imagen', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
