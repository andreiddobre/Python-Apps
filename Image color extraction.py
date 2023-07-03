#pip install PIL

from PIL import Image
Image.open('leaves.jpg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('leaves.jpg')
w, h, d = tuple(image.shape)
pixels = np.reshape(image, (w * h, d))
from sklearn.cluster import KMeans
n_colors = 3 #nr of colors
model = KMeans(n_clusters = n_colors, random_state = 42).fit(pixels)
palette = np.uint8(model.cluster_centers_)
plt.imshow([palette])
plt.show()

#code inspired by clcoding.com
