'''
Created on May 3, 2024

@author: NGO ANH TUAN
'''
import random

import cv2
import scipy

import matplotlib.pyplot as plt
import numpy as np
def midpoint(x):
    return 0.5 * (max(x) + min(x))
def alpha_trimmed(x,d):
    x_sort = np.sort(x.ravel())  # Sort values and flatten the array
    low_lim = int(d / 2) + 1
    hi_lim = np.prod(x.shape) - int(d / 2)

    newx = x_sort[low_lim:hi_lim]  # Extract values within limit indices
    y = np.mean(newx)
    return y
def add_gauss_noise(image, mean, std):
    gaussian_noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    # Thêm nhiễu vào ảnh
    noisy_image = cv2.add(image, gaussian_noise)
    return noisy_image
def add_salt_and_pepper_noise(img):
    row , col = img.shape 
      
    # Randomly pick some pixels in the 
    # image for coloring them white 
    # Pick a random number between 300 and 10000 
    number_of_pixels = random.randint(300, 10000) 
    for i in range(number_of_pixels): 
        
        # Pick a random y coordinate 
        y_coord=random.randint(0, row - 1) 
          
        # Pick a random x coordinate 
        x_coord=random.randint(0, col - 1) 
          
        # Color that pixel to white 
        img[y_coord][x_coord] = 255
          
    # Randomly pick some pixels in 
    # the image for coloring them black 
    # Pick a random number between 300 and 10000 
    number_of_pixels = random.randint(300 , 10000) 
    for i in range(number_of_pixels): 
        
        # Pick a random y coordinate 
        y_coord=random.randint(0, row - 1) 
          
        # Pick a random x coordinate 
        x_coord=random.randint(0, col - 1) 
          
        # Color that pixel to black 
        img[y_coord][x_coord] = 0
          
    return img 
if __name__ == '__main__':
    image = cv2.imread("cameraman2.tif")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise_image = cv2.imread("cameraman2.tif")
    noise_image = cv2.cvtColor(noise_image, cv2.COLOR_BGR2GRAY)
    add_salt_and_pepper_noise(noise_image)
    filtered_image = scipy.signal.medfilt2d(noise_image, kernel_size=3)
    
    plt.subplot(331)
    plt.imshow(image, cmap="gray")
    plt.title("Original image")
    plt.axis('off')
    
    plt.subplot(332)
    plt.imshow(noise_image, cmap="gray")
    plt.title("Pepper and salt image")
    plt.axis('off')
    
    plt.subplot(333)
    plt.imshow(filtered_image, cmap="gray")
    plt.title("Pepper and salt remove with median")
    plt.axis('off')
    # gauss
    gauss_noise_image = add_gauss_noise(image,0,1)
    plt.subplot(334)
    plt.imshow(gauss_noise_image, cmap="gray")
    plt.title("Gauss noise image")
    plt.axis('off')
    
    gauss_remove_image = scipy.signal.medfilt2d(gauss_noise_image.astype(np.float32), kernel_size=3)
    plt.subplot(335)
    plt.imshow(gauss_remove_image, cmap="gray")
    plt.title("Gauss noise remove with median")
    plt.axis('off')
    # order filter(min filter)
    gauss_remove_image_1 = scipy.signal.order_filter(gauss_noise_image.astype(np.float32),np.ones((3,3)), 1)
    plt.subplot(336)
    plt.imshow(gauss_remove_image_1, cmap="gray")
    plt.title("Gauss noise remove with order(min) filter")
    plt.axis('off')
    # midpoint filter
    gauss_remove_image_2 = scipy.ndimage.generic_filter(gauss_noise_image, midpoint, size=(3, 3))
    plt.subplot(337)
    plt.imshow(gauss_remove_image_2, cmap="gray")
    plt.title("Gauss noise remove with midpoint filter")
    plt.axis('off')
    # Alpha-Trimmed Mean Filters
    gauss_remove_image_3 = scipy.ndimage.generic_filter(gauss_noise_image, alpha_trimmed, size=(3, 3),extra_arguments =(6,))
    plt.subplot(338)
    plt.imshow(gauss_remove_image_3, cmap="gray")
    plt.title("Gauss noise remove with Alpha-Trimmed")
    plt.axis('off')
    
    plt.show()