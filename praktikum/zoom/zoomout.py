import numpy as np
import imageio.v2 as img  
import matplotlib.pyplot as plt

def zoom_out(image, factor):
    height, width = image.shape[:2]
    new_height = int(height / factor)
    new_width = int(width / factor)
    img_zoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y * factor)
            ori_x = int(x * factor)

            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            img_zoom[y, x] = image[ori_y, ori_x]

    return img_zoom

image = img.imread('C://SMT_5//Pengolahan_Citra//praktikum//images.jpg')
scale = 2.0  

img_zoom = zoom_out(image, scale)

img.imwrite("C://SMT_5//Pengolahan_Citra//praktikum//Z.jpg", img_zoom)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_zoom)
plt.title('Zoomed Out Image')
plt.axis('off')

plt.show()
