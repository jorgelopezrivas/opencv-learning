import numpy as np
import cv2
from matplotlib import pyplot as plt

# Noise Exercises
# Types of noise: Gaussian, Rayleigh, Gamma, Exponential, Uniform, Impulse (salt & pepper)


img = cv2.imread('./images/standard_images/fig0503.tif',0)

# Gaussian:
# randn fills the array with normally distributed random numbers
# randn(dest, mean, stddev)
gaussian_noise = np.zeros((img.shape[0], img.shape[1]), np.uint8)
cv2.randn(gaussian_noise, (128), (10))
res1 = img + gaussian_noise
median = cv2.medianBlur(res1,29)

# plot all the images and their histograms
images = [img, gaussian_noise, res1, median]
titles = ['Original Image','Histogram','Global Thresholding (v=127)']
#          'Original Noisy Image','Histogram',"Otsu's Thresholding",
#          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

nrows = 4
for i in xrange(nrows):
    #plt.subplot(nrows, ncols, plot_number)
    plt.subplot(nrows,2,i*2+1),plt.imshow(images[i],'gray')
    #ravel returns a contiguous flattened array
    plt.subplot(nrows,2,i*2+2),plt.hist(images[i].ravel(),256, [0,256])
plt.show()
