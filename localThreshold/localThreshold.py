import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def localThres(image,blok_size,c):
    imgPad = np.pad(image,pad_width=1,mode='constant', constant_values=0)
    threshold = np.zeros_like(image)

    for i in range(image.shape[1]):
        for j in range(image.shape[1]):
            local_area = imgPad[i:i+blok_size,j:j+blok_size]
            local_mean = np.mean(local_area)
            threshold[i,j] = 255 if image[i][j] > (local_mean - c) else 0
    return threshold

image1 = img.imread('C://taufikH//localThreshold//download.jpg', mode='F')
image2 = img.imread('C://taufikH//localThreshold//download.jpg')

thres = localThres(image1,15,10)
mask = (thres==255).astype(np.uint8)
segmented = image2 * mask[:,:,np.newaxis]

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(image2)

plt.subplot(1,3,2)
plt.imshow(thres,cmap='gray')

plt.subplot(1,3,3)
plt.imshow(segmented)
plt.show()

