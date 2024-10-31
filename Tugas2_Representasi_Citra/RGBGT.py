import numpy as np
import imageio.v2 as imageio  
import matplotlib.pyplot as plt

def load_image(image_path):
    return imageio.imread(image_path)


def get_red_channel(image):
    red_channel = image.copy()
    red_channel[:, :, 1] = 0  
    red_channel[:, :, 2] = 0  
    return red_channel


def get_green_channel(image):
    green_channel = image.copy()
    green_channel[:, :, 0] = 0  
    green_channel[:, :, 2] = 0  
    return green_channel


def get_blue_channel(image):
    blue_channel = image.copy()
    blue_channel[:, :, 0] = 0  
    blue_channel[:, :, 1] = 0  
    return blue_channel


def convert_to_grayscale(image):
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale_image


def convert_to_binary(image, threshold=128):
    grayscale_image = convert_to_grayscale(image)
    binary_image = (grayscale_image > threshold).astype(np.uint8) * 255
    return binary_image


image_paths = [
    ('pepaya.jpg', 'Pepaya'),
    ('singkong.jpg', 'Singkong'),
    ('kenikir.jpg', 'Kenikir')
]

titles = ["Red Channel", "Green Channel", "Blue Channel", "Grayscale Image", "Binary Image"]

fig, axes = plt.subplots(len(image_paths), len(titles), figsize=(20, 15))

for row, (image_path, label) in enumerate(image_paths):
    
    image = load_image(image_path)
    
    red_channel = get_red_channel(image)
    green_channel = get_green_channel(image)
    blue_channel = get_blue_channel(image)
    grayscale_image = convert_to_grayscale(image)
    binary_image = convert_to_binary(image, threshold=128)
    
    
    images = [red_channel, green_channel, blue_channel, grayscale_image, binary_image]
    
    for col, (img, title) in enumerate(zip(images, titles)):
        ax = axes[row, col]
        ax.imshow(img, cmap='gray' if img.ndim == 2 else None)
        if row == 0:
            ax.set_title(title)
        ax.axis('off')

    
    axes[row, 0].annotate(label, xy=(-0.1, 0.5), xycoords="axes fraction", 
                          ha="center", va="center", fontsize=14, rotation=90)


plt.tight_layout()
plt.show()


