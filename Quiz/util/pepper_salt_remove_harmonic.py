'''
Created on May 3, 2024

@author: NGO ANH TUAN
'''
import cv2
import scipy
import numpy as np
import matplotlib.pyplot as plt

def harmonic(x):
    # Filter out zeros
    bad_indices = np.where(x == 0)
    newx = np.delete(x, bad_indices)

    # Calculate the modified harmonic mean
    newx_adj = 1.0 / newx
    mysum = np.sum(newx_adj)

    # Compute the result
    y = np.prod(x.shape) / mysum
    return y

def add_gauss_noise(image,mean,std):
    gaussian_noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    # Thêm nhiễu vào ảnh
    noisy_image = cv2.add(image, gaussian_noise)
    return noisy_image

if __name__ == '__main__':
    # salt
    salt_image = cv2.imread("eight_salt.tif")
    salt_image = cv2.cvtColor(salt_image, cv2.COLOR_BGR2GRAY)
    salt_removed_image = scipy.ndimage.generic_filter(salt_image, harmonic, size=(3, 3))
    plt.subplot(321)
    plt.imshow(salt_image, cmap="gray")
    plt.title("Salt Image")
    plt.axis('off')
    
    plt.subplot(322)
    plt.imshow(salt_removed_image, cmap="gray")
    plt.title("Salt Removed with harmonic(success)")
    plt.axis('off')
    # pepper
    pepper_image = cv2.imread("eight_pepper.tif")
    pepper_image = cv2.cvtColor(pepper_image, cv2.COLOR_BGR2GRAY)
    pepper_removed_image = scipy.ndimage.generic_filter(pepper_image, harmonic, size=(3, 3))
    plt.subplot(323)
    plt.imshow(pepper_image, cmap="gray")
    plt.title("Pepper Image")
    plt.axis('off')
    
    plt.subplot(324)
    plt.imshow(pepper_removed_image, cmap="gray")
    plt.title("Pepper Removed with harmonic(false)")
    plt.axis('off')
    
    
    image3 = cv2.imread("cameraman2.tif")
    image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
    noise_image = add_gauss_noise(image3,0,1) 
    gauss_removed_image = scipy.ndimage.generic_filter(image3.astype(np.float32), harmonic, size=(3, 3))
    
    plt.subplot(325)
    plt.imshow(noise_image, cmap="gray")
    plt.title("Gauss noise image")
    plt.axis('off')
    
    plt.subplot(326)
    plt.imshow(gauss_removed_image, cmap="gray")
    plt.title("Gauss Removed with harmonic")
    plt.axis('off')
    
    plt.show()