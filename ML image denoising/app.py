"""
@author: github.com/kralchris

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# Load
image = plt.imread("noisy_image.jpg")

# Display
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

# Apply denoising
denoised_image = ndimage.median_filter(image, size=3)

# Display the denoised image
plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image')
plt.axis('off')

plt.tight_layout()
plt.show()
