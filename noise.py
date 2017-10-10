import numpy as np
import cv2
from matplotlib import pyplot as plt

# Noise Exercises
# Types of noise: Gaussian, Rayleigh, Gamma, Exponential, Uniform, Impulse (salt & pepper)


img = cv2.imread('./images/standard_images/cameraman.tif',0)
#generate different types of noise:

# Gaussian:
# randn fills the array with normally distributed random numbers
# randn(dest, mean, stddev)
gaussian_noise = np.zeros((img.shape[0], img.shape[1]), np.uint8)
cv2.randn(gaussian_noise, (1), (30))
res1 = img + gaussian_noise


# plot all the images and their histograms
images = [img, gaussian_noise, res1]
titles = ['Original Image','Histogram','Global Thresholding (v=127)']
#          'Original Noisy Image','Histogram',"Otsu's Thresholding",
#          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]



#plt.subplot(1,2,1)
#plt.imshow(img2, 'gray')
#plt.subplot(1,2,2)
#plt.hist(img2.ravel(), 256)		
#plt.show()

for i in xrange(3):
    #plt.subplot(nrows, ncols, plot_number)
    plt.subplot(3,2,i*2+1),plt.imshow(images[i],'gray')
    #ravel returns a contiguous flattened array
    plt.subplot(3,2,i*2+2),plt.hist(images[i].ravel(),256)
plt.show()
