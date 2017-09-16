import numpy as np

def getBlankImage(height, width, bgColor=(255, 255, 255)):
	# Create white blank image
	image = np.zeros((height, width, 3), np.uint8)
	
	#Convert to BGR
	color = tuple(reversed(bgColor))
	image[:] = color
	
	return image
