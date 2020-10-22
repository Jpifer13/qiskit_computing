import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def show_mpl_image(resource_image: PIL.Image):
    img = np.array(resource_image.open(), dtype=np.uint8)
    fig, ax = plt.subplots(1)
    ax.imshow(img)
    plt.show()