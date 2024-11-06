#Dilation
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image is binary (optional, depending on your image)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel for dilation (you can change the shape and size)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Perform dilation
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Display the original and dilated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilated_image, cmap='gray')
plt.title('Dilated Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the dilated image
cv2.imwrite('dilated_image.jpg', dilated_image)


#Erosion
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image is binary (optional, depending on your image)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel for erosion (you can change the shape and size)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Perform erosion
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Display the original and eroded images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title('Eroded Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the eroded image
cv2.imwrite('eroded_image.jpg', eroded_image)

#Opening
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image is binary (optional, depending on your image)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel for opening (you can change the shape and size)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Perform opening
opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

# Display the original and opened images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(opened_image, cmap='gray')
plt.title('Opened Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the opened image
cv2.imwrite('opened_image.jpg', opened_image)

#Closing
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image is binary (optional, depending on your image)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel for closing (you can change the shape and size)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Perform closing
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Display the original and closed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(closed_image, cmap='gray')
plt.title('Closed Image')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the closed image
cv2.imwrite('closed_image.jpg', closed_image)

#Hit-or-Mass Transformation
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Ensure the image is binary (optional, depending on your image)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a hit-or-miss kernel (structuring element)
# Here we define a simple cross shape for demonstration
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

# Perform hit-or-miss transformation
# To perform hit-or-miss, we need to use cv2.morphologyEx with cv2.MORPH_HITMISS
hit_or_miss_result = cv2.morphologyEx(binary_image, cv2.MORPH_HITMISS, kernel)

# Display the original and hit-or-miss images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(hit_or_miss_result, cmap='gray')
plt.title('Hit-or-Miss Transformation')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the hit-or-miss image
cv2.imwrite('hit_or_miss_image.jpg', hit_or_miss_result)

