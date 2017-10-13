import numpy as np
import cv2
from matplotlib import pyplot as plt
# Noise Exercises
# Types of noise: 
#	1) Gaussian
#	2) Rayleigh, 
#	3) Gamma, 
#	4) Exponential, 
#	5) Uniform, 
#	6) Impulse (salt & pepper)

def gaussian_noise(src, mean, stddev):
	noise = np.zeros((src.shape[0], src.shape[1]), np.uint8)
	# randn fills the array with normally distributed random numbers
	# randn(dest, mean, stddev)
	cv2.randn(noise, (mean), (stddev))	
	dst = src + noise
	return dst, noise
	
def rayleigh_noise()

	return dst, noise
	
def gamma_noise()

	return dst, noise
	
def exponential_noise()

	return dst, noise
	
def uniform_noise(src, low, high):
	noise = np.random.uniform(low, high, src.shape[0]*src.shape[1])
	noise = noise.reshape(src.shape[0], src.shape[1]).astype(np.uint8)
	dst = src + noise	
	return dst, noise
	
def impulse_noise()

	return dst, noise
	
img = cv2.imread('./images/standard_images/fig0503.tif',0)
plot = 1
plots = ['Gaussian Noise', 'Uniform Noise']
titles = ['Original', 'Noise', 'Noise Added', 'Media Filter']
for _ in plots:
	nrows = 4	
	plt.figure(plot)
	if plot == 1:
		# Gaussian
		res, noise = gaussian_noise(img, 0, 20)
	elif plot == 2:
		# Uniform
		res, noise = uniform_noise(img, 50, 100)
		
	median = cv2.medianBlur(res, 11)
	images = [img, noise, res, median]
	
	for i in xrange(nrows):
		#plt.subplot(nrows, ncols, plot_number)
		plt.subplot(nrows, 2, i*2+1),plt.imshow(images[i], 'gray')
		plt.xticks([]),plt.yticks([])
		plt.title(titles[i])
		#ravel returns a contiguous flattened array
		plt.subplot(nrows,2,i*2+2),plt.hist(images[i].ravel(),256, [0,256])
		plt.xlim(0,255)
	plt.show()
	plot += 1
