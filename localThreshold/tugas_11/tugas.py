import numpy as np
import imageio.v3
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

def sobel_edge_detection(image):
    
    sobel_x = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])
    
    sobel_y = np.array([[1, 2, 1],
                         [0, 0, 0],
                         [-1, -2, -1]])
    
    gradient_x = convolve(image, sobel_x)
    gradient_y = convolve(image, sobel_y)
    
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    return gradient_magnitude

def thresholding(image, threshold):
    
    binary_image = (image > threshold).astype(np.uint8) * 255
    return binary_image

image_path = 'C://sesi9//openmap//download.jpg'  
image = imageio.v3.imread(image_path, mode='F')

edges = sobel_edge_detection(image)

threshold_value = 50  
segmented_image = thresholding(edges, threshold_value)

plt.figure(figsize=(12, 8))

plt.subplot(1, 3, 1)
plt.title('Citra Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Deteksi Tepi (Sobel)')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Segmentasi Citra')
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()