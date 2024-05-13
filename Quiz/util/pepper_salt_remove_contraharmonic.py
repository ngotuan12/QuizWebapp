'''
Created on May 3, 2024

@author: NGO ANH TUAN
'''

import cv2
import scipy
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic(x, r):
    num = np.sum(x**(r + 1))
    den = np.sum(x**r)
    return num / den

def pepper_remove(image):
    return scipy.ndimage.generic_filter(image, contraharmonic, size=(3, 3),extra_arguments =(1,))
def salt_remove(image):
    return scipy.ndimage.generic_filter(image, contraharmonic, size=(3, 3),extra_arguments =(-1,))
if __name__ == '__main__':
    # pepper remove
    image = cv2.imread("eight_pepper.tif")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pepper_removed_image = pepper_remove(image)
    
    plt.subplot(221)
    plt.imshow(image, cmap="gray")
    plt.title("Pepper Image")
    plt.axis('off')
    
    plt.subplot(222)
    plt.imshow(pepper_removed_image, cmap="gray")
    plt.title("Pepper Removed")
    plt.axis('off')
    # salt remove
    image2 = cv2.imread("eight_salt.tif")
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    salt_removed_image = salt_remove(image2)
    
    plt.subplot(223)
    plt.imshow(image2, cmap="gray")
    plt.title("Salt Image")
    plt.axis('off')
    
    plt.subplot(224)
    plt.imshow(salt_removed_image, cmap="gray")
    plt.title("Salt Removed")
    plt.axis('off')
    
    plt.show()