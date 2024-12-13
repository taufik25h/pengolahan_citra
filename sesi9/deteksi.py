import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Membaca gambar
image = imageio.imread("C://taufikH//download.jpg", mode='F')

# Operator Roberts
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])

# Menghitung deteksi tepi dengan Roberts
edges_roberts_x = convolve(image, roberts_x)
edges_roberts_y = convolve(image, roberts_y)
edges_roberts = np.hypot(edges_roberts_x, edges_roberts_y)

# Operator Sobel
sobel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# Menghitung deteksi tepi dengan Sobel
edges_sobel_x = convolve(image, sobel_x)
edges_sobel_y = convolve(image, sobel_y)
edges_sobel = np.hypot(edges_sobel_x, edges_sobel_y)

# Menampilkan hasil
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Gambar Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Deteksi Tepi Roberts')
plt.imshow(edges_roberts, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Deteksi Tepi Sobel')
plt.imshow(edges_sobel, cmap='gray')
plt.axis('off')

plt.show()