import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load in grayscale

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Save the equalized image
cv2.imwrite('equalized_image.jpg', equalized_image)

# Display the equalized image
cv2_imshow(equalized_image)

import cv2
import matplotlib.pyplot as plt

# Load the original image
image_path = '/content/mr.bean.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(original_image)

# Calculate histograms
original_hist = cv2.calcHist([original_image], [0], None, [256], [0, 256])
equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(12, 6))

# Original image histogram
plt.subplot(1, 2, 1)
plt.plot(original_hist, color='black')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])
plt.grid()

# Equalized image histogram
plt.subplot(1, 2, 2)
plt.plot(equalized_hist, color='black')
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])
plt.grid()

plt.tight_layout()
plt.show()
