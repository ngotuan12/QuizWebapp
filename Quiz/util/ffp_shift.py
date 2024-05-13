'''
Created on Apr 24, 2024

@author: Administrator
'''


# Load the image
# image = cv2.imread("tuanna.jpg")
#
# # Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Compute the DFT
# fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
#
# # Shift the zero-frequency component
# dft_shift = np.fft.fftshift(fourier)
#
# # Compute the magnitude
# magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])
#
# # Scale the magnitude for visualization
# magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
#
# # Display the magnitude
# plt.imshow(magnitude, cmap="gray")
# plt.title("Fourier Transform Magnitude")
# plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy

image = cv2.imread("cameraman2.tif")

# Chuyển sang ảnh xám
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(131)
plt.imshow(image, cmap="gray")
plt.title("original image")
plt.axis("off")
# Chuyển sang miền tần số
fft2 = scipy.fft.fft2(image.astype(np.float32))

fft2_shifted = scipy.fft.fftshift(fft2)

# Phổ ánh sáng của ảnh(Phải chuyển ảnh sang ảnh xám)
spectrum_image = np.log(1+ np.abs(fft2_shifted))
plt.subplot(132)
plt.imshow(spectrum_image, cmap="gray")
plt.title("spectrum image")
plt.axis("off")

# Thuật toán biến đổi ảnh
# Thao tác với fft2_shifted

# ... Viết code ở đây

# Dịch ngược lại ảnh
ifft2_shifted = scipy.fft.ifftshift(fft2_shifted)
ifft2 = scipy.fft.ifft2(ifft2_shifted)

image2  = np.real(ifft2)

plt.subplot(133)
plt.imshow(image2, cmap="gray")
plt.title("itft2 image")
plt.axis("off")
plt.show()
# magnitude = cv2.magnitude(fft2_shifted[:, :, 0], fft2_shifted[:, :, 1])
#
# # Scale the magnitude for visualization
# magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
# plt.subplot(122)
# plt.imshow(magnitude_spectrum, cmap="gray")

# cv2.imshow('shifted image',magnitude)
# cv2.waitKey(0)
# plt.figure(figsize=(10, 5))
#
# plt.subplot(121)
# plt.imshow(image, cmap="gray")
# plt.title("Original Image")
# plt.axis("off")
#
# plt.subplot(122)
# plt.imshow(magnitude_spectrum, cmap="gray")
# plt.title("Magnitude Spectrum (log scale)")
# plt.axis("off")

# plt.show()
