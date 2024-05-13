'''
Created on May 2, 2024

@author: NGO ANH TUAN
'''
import cv2
import scipy
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("eight_salt.tif")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_double = image.astype(np.float32)

image_fft2 = scipy.fft.fft2(image_double)

M, N = image.shape

dist = scipy.spatial.distance_matrix(np.arange(M).reshape(M, 1), np.arange(N).reshape(N, 1))

plt.subplot(521)
plt.imshow(image, cmap="gray")
plt.title("Original image")
plt.axis('off')


fft2_shifted = scipy.fft.fftshift(image_fft2)

# Phổ ánh sáng của ảnh(Phải chuyển ảnh sang ảnh xám)
spectrum_image = np.log(1+ np.abs(fft2_shifted))

plt.subplot(522)
plt.imshow(spectrum_image, cmap="gray")
plt.title("spectrum image")
plt.axis('off')

plt.subplot(523)
plt.imshow(scipy.fft.fftshift(dist), cmap="gray")
plt.title("Distance matrix")
plt.axis('off')

# Ideal filter

H = np.ones((M, N))
radius = 30
ind = dist <= radius
H[ind] = 0
a = 1 
b = 1
Hd = a + (b * H)
DFT_filts = Hd.astype(np.float32)
image2 = np.real(scipy.fft.ifft2(DFT_filts*image_fft2))
plt.subplot(525)
plt.imshow(scipy.fft.fftshift(DFT_filts), cmap="gray")
plt.title("Ideal high-passs")
plt.axis('off')

plt.subplot(526)
plt.imshow(image2, cmap="gray")
plt.title("Image filtered with ideal")
plt.axis('off')

# Gauss
sigma = 30
H_gau = 1- np.exp(-(dist ** 2) / (2 * (sigma ** 2)))
DFT_filt_gau =  a + (b * H_gau)
image3 = np.real(scipy.fft.ifft2(DFT_filt_gau*image_fft2))

plt.subplot(527)
plt.imshow(scipy.fft.fftshift(DFT_filt_gau), cmap="gray")
plt.title("Gaussian high-passs")
plt.axis('off')

plt.subplot(528)
plt.imshow(image3, cmap="gray")
plt.title("Gaussian image filtered")
plt.axis('off')

# Butterworth
cutoff = 30; 
order = 2;
H_but = 1 / (1 + (cutoff / dist) ** (2 * order))

DFT_filt_but =  a + (b * H_but)

image4 = np.real(scipy.fft.ifft2(DFT_filt_but * image_fft2))

plt.subplot(529)
plt.imshow(scipy.fft.fftshift(DFT_filt_but), cmap="gray")
plt.title("Butterworth high-passs")
plt.axis('off')

plt.subplot(5,2,10)
plt.imshow(image4, cmap="gray")
plt.title("Butterworth image filtered")
plt.axis('off')

plt.show()