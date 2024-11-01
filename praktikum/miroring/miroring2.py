import numpy as np
import imageio.v2 as img  
import matplotlib.pyplot as plt

path = 'C://SMT_5//Pengolahan_Citra//praktikum//images2.jpg'
image = img.imread(path)

height, width = image.shape[:2]

horizontal_vertical = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        horizontal_vertical[y, x] = image[height - 1 - y, width - 1 - x]


plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 2, 2)
plt.imshow(horizontal_vertical)
plt.title("Mirroring Horizontal & Vertikal Bersamaan")

plt.show()
