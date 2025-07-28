import matplotlib.pyplot as plt 
import numpy as np 

def show_img_fig(image, ax, title = 'img', cmap_type = 'gray'):
    ax.imshow(image, cmap = cmap_type)
    ax.set_title(title)
    ax.axis('off')

def show_image(image, title = 'Image', cmap_type = 'gray'):
    plt.imshow(image, cmap = cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()