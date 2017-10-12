import numpy as np
import cv2
import time
from matplotlib import pyplot as plt

# Capture x seconds of video as frames
captureTime =  0.067
capture = cv2.VideoCapture(0)

# Find OpenCV version and get fps
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver)  < 3 :
	fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
	print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
else :
	fps = capture.get(cv2.CAP_PROP_FPS)
	print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
     

frames = captureTime * fps
dontSaveFrames = 10
path = './saved_frames/'
width = capture.get(3)  
height = capture.get(4)
average = np.zeros((height, width), np.uint8)
i = 0

while(i < frames + dontSaveFrames):
	ret,frame = capture.read()
	if(i >= dontSaveFrames):	
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imwrite(path + "frame-%d.jpg" % (i-dontSaveFrames), gray)
		average = average + (gray / frames)
	i += 1

capture.release()
cv2.imwrite(path + "average.jpeg", average)
