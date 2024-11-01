import numpy as np
import imageio.v2 as img  
import matplotlib.pyplot as plt

path = 'C://SMT_5//Pengolahan_Citra//praktikum//images2.jpg'
image = img.imread(path)

height, width = image.shape[:2]
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        horizontal[y, x] = image[y, width - 1 - x]

for y in range(height):
    for x in range(width):
        vertical[y, x] = image[height - 1-y, x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image)

plt.subplot(1, 3, 2)
plt.imshow(horizontal)

plt.subplot(1, 3, 3)
plt.imshow(vertical)

plt.show()