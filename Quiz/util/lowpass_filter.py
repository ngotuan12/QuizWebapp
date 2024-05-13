'''
Created on May 2, 2024

@author: NGO ANH TUAN
'''
import cv2
import scipy
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("eight_pepper.tif")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_double = image.astype(np.float32)

image_fft2 = scipy.fft.fft2(image_double)

M, N = image.shape

dist = scipy.spatial.distance_matrix(np.arange(M).reshape(M, 1), np.arange(N).reshape(N, 1))

sigma = 30
H_gau = np.exp(-(dist ** 2) / (2 * (sigma ** 2)))

plt.subplot(241)
plt.imshow(scipy.fft.fftshift(dist), cmap="gray")
plt.title("Distance matrix")
plt.axis('off')

plt.subplot(242)
plt.imshow(image, cmap="gray")
plt.title("Original image")
plt.axis('off')

plt.subplot(243)
plt.imshow(scipy.fft.fftshift(H_gau), cmap="gray")
plt.title("Gaussian low-passs")
plt.axis('off')
#Filter the FT image with the Gaussian low-pass filter and display the filtered image
DFT_filt_gau = H_gau * image_fft2
image3 = np.real(scipy.fft.ifft2(DFT_filt_gau))
plt.subplot(244)
plt.imshow(image3, cmap="gray")
plt.title("Filtered Image by gaussian")
plt.axis('off')

#
H = np.zeros((M, N))
radius = 35
ind = dist <= radius
H[ind] = 1
Hd = H.astype(float)
plt.subplot(245)
plt.imshow(scipy.fft.fftshift(Hd), cmap="gray")
plt.title("Ideal low-passs")
plt.axis('off')

DFT_filt_Hd = Hd * image_fft2
image2 = np.real(scipy.fft.ifft2(DFT_filt_Hd))
plt.subplot(246)
plt.imshow(image2, cmap="gray")
plt.title("Filtered Image by Ideal")
plt.axis('off')

#Butterworth
D0 = 35
n = 3
H_but = 1 / (1 + (dist / D0) ** (2 * n))
plt.subplot(247)
plt.imshow(scipy.fft.fftshift(H_but), cmap="gray")
plt.title("Butterworth low-passs")
plt.axis('off')


DFT_filt_but = H_but * image_fft2
image4 = np.real(scipy.fft.ifft2(DFT_filt_but))
plt.subplot(248)
plt.imshow(image4, cmap="gray")
plt.title("Filtered Image by Butterworth")
plt.axis('off')

plt.show()