import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./images/fap.jpg')
image = cv2.medianBlur(image,7)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

dst1 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,15,1)
            
kernel = np.ones((5,5),np.float32)/25
dst2 = cv2.filter2D(dst1,-1,kernel)
        
dst3, contours, hierarchy = cv2.findContours(dst2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(dst2, contours, 1, (0,255,0), 3)
cv2.imshow("asdfg",dst2)
cv2.imshow("asdf",dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
            


#Floodfill
#dst3 = dst2.copy()
#h, w = dst3.shape[:2]
#mask = np.zeros((h+2, w+2), np.uint8)
#cv2.floodFill(dst3, mask, (0,0), 255);
#im_floodfill_inv = cv2.bitwise_not(dst3)

#imagePreview = dst2.copy()
#im2, contours, hierarchy = cv2.findContours(dst2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#for contour in contours:
    #epsilon = 0.001 * cv2.arcLength(contour,True)
    #cv2.drawContours(imagePreview, [cv2.approxPolyDP(contour, epsilon, True)], 0, (0,255,0), 1)
#	cv2.drawContours(imagePreview, [contour], 0, (0,255,0), 1)
#cv2.imshow("drawContours", im2)
            
#titles = ['Source', 'adaptive Th', 'Filtered', 'contour']
#images = [image, dst1, dst2, imagePreview]

#for i in xrange(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

