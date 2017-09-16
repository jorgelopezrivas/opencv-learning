import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3, 320);
cap.set(4, 240);

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

#out = cv2.VideoWriter('output.avi',fourcc, 10, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        #out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
