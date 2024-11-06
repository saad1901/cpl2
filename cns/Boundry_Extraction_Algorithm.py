import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the binary image (ensure it's in binary format)
image_path = '/content/mr.bean.jpg'
binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply a threshold to ensure it's a binary image (optional, if image is not already binary)
_, binary_image = cv2.threshold(binary_image, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty image to draw the boundaries
boundary_image = np.zeros_like(binary_image)

# Draw contours on the boundary image
cv2.drawContours(boundary_image, contours, -1, (255), thickness=1)

# Display the original and boundary images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(boundary_image, cmap='gray')
plt.title('Extracted Boundary Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the boundary image
cv2.imwrite('extracted_boundary_image.jpg', boundary_image)