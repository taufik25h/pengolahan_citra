import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import sobel


image = imageio.imread('C://latihan//download.jpg')

if len(image.shape) == 3:
    gray_image = np.mean(image, axis=2) 
else:
    gray_image = image

sobel_x = sobel(gray_image, axis=0)  
sobel_y = sobel(gray_image, axis=1)  
sobel_magnitude = np.hypot(sobel_x, sobel_y)  

sobel_magnitude = (sobel_magnitude / np.max(sobel_magnitude)) * 255
sobel_magnitude = sobel_magnitude.astype(np.uint8)

threshold_value = 100 
segmented_image = (sobel_magnitude > threshold_value) * 255 

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title('Gambar Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Deteksi Sobel')
plt.imshow(sobel_magnitude, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Segmentasi Citra')
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()