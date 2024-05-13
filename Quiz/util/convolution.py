'''
Created on May 2, 2024

@author: NGO ANH TUANs
'''
import numpy as np
from scipy import ndimage
import cv2
def create_gaussian_array_filter(size, sigma):
    siz = (size - 1) / 2
    x, y = np.meshgrid(np.arange(-siz, siz + 1), np.arange(-siz, siz + 1))
    arg = -(x**2 + y**2) / (2 * sigma**2)
    h = np.exp(arg)
    h[h < np.finfo(float).eps * np.max(h)] = 0
    sum_h = np.sum(h)
    if sum_h != 0:
        h /= sum_h
    return h
low_pass_filter = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])
#
high_pass_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

horizontal_edge_detection = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

array_input = np.array([
                            [5, 8, 3, 4, 6, 2, 3, 7], 
                            [3, 2, 1, 1, 9, 5, 1, 0], 
                            [0, 9, 5, 3, 0, 4, 8, 3],
                            [4, 2, 7, 2, 1, 9, 0, 6], 
                            [9, 7, 9, 8, 0, 4, 2, 4], 
                            [5, 2, 1, 8, 4, 1, 0, 9],
                            [1, 8, 5, 4, 9, 2, 3, 8], 
                            [3, 7, 1, 2, 3, 4, 4, 6]
                        ])
array_filter = np.array([[2, 1, 0], [1, 1, -1], [0, -1, -2]])
array_output = ndimage.convolve(array_input, array_filter, mode='constant', cval=0.0)
print(array_output)
array_output = ndimage.correlate(array_input, array_filter)
print(array_output)
# mean filter
array_output = ndimage.uniform_filter(array_input, size=1.1)
print(array_output)

image = cv2.imread('cameraman2.tif', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original image', image)

filtered_image = ndimage.uniform_filter(image, size=5)

cv2.imshow('Filtered image', filtered_image)

array_filter = np.array([[1,2,1],[2,4,2],[1,2,1]]) * 1/16

filtered_image_2 = ndimage.convolve(image,array_filter, mode='constant', cval=0.0)

cv2.imshow('Filtered image 2', filtered_image_2)
kernel_size = 9 // 2
#The Gaussian kernel will have size 2*radius + 1 along each axis. If radius is None, the default radius = round(truncate * sigma) will be used
gaussian_filter = ndimage.gaussian_filter(image, sigma=1,radius=1,truncate=0)

cv2.imshow('Gaussian filter image', gaussian_filter)
laplace = ndimage.laplace(image)

cv2.imshow('laplace filter image', laplace)
cv2.waitKey(0)