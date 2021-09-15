# Python code to convert an image to ASCII image.
import sys, random, argparse
import numpy as np
import math
import cv2

from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '

def getAverageL(image):

	"""
	Given PIL Image, return average value of grayscale value
	"""
	# get image as numpy array
	im = np.array(image)

	# get shape
	w,h,l = im.shape

	# get average
	return np.average(im.reshape(w,h,l))


def convertImageToAscii(frame, cols, scale, moreLevels):
	"""
	Given Image and dims (rows, cols) returns an m*n list of Images
	"""
	# declare globals
	global gscale1, gscale2

	# open image and convert to grayscale
	image = Image.fromarray(frame)

	# store dimensions
	W, H = image.size[0], image.size[1]

	# compute width of tile
	w = W/cols

	# compute tile height based on aspect ratio and scale
	h = w/scale

	# compute number of rows
	rows = int(H/h)
	
	# check if image size is too small
	if cols > W or rows > H:
		exit(0)

	# ascii image is a list of character strings
	jArray = []
	# generate list of dimensions
	for j in range(rows):
		y1 = int(j*h)
		y2 = int((j+1)*h)

		# correct last tile
		if j == rows-1:
			y2 = H

		iArray = []

		for i in range(cols):

			# crop image to tile
			x1 = int(i*w)
			x2 = int((i+1)*w)

			# correct last tile
			if i == cols-1:
				x2 = W

			# crop image to extract tile
			img = image.crop(( int(i*w), y1, x2, y2))

			# get average luminance
			avg = int(getAverageL(img))

			# look up ascii char
			if moreLevels:
				gsval = gscale1[int((avg*69)/255)]
			else:
				gsval = gscale2[int((avg*9)/255)]

			# append ascii char to string
			pixel = img.getpixel((w/2,h/2))
			#numval = int((pixel[0] + pixel[1] + pixel[2]) / 77)
			iArray.append((gsval, (pixel[0],pixel[1],pixel[2])))
		jArray.append(iArray)
	
	# return txt image
	return jArray
