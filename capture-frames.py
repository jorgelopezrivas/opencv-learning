import numpy as np
import cv2
from matplotlib import pyplot as plt

# Capture certain number of frames
frames = 9
path = './saved_frames/'

cap = cv2.VideoCapture(0)
width = cap.get(3)  
height = cap.get(4)
average = np.zeros((height, width), np.uint8)
i = 0

while(i < frames):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imwrite(path + "frame-%d.jpg" % i, gray)
	average = average + (gray / frames)
	i += 1

cap.release()
cv2.imwrite(path + "combined.jpg", average)

