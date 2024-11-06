#Negate the image
import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path)

# Negate the image
negated_image = 255 - image

# Save the negated image
cv2.imwrite('negated_image.jpg', negated_image)

# Display the negated image
cv2_imshow(negated_image)


#Thresholding of an image
import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load in grayscale

# Apply thresholding
threshold_value = 127  # You can adjust this value
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Save the thresholded image
cv2.imwrite('thresholded_image.jpg', thresholded_image)

# Display the thresholded image
cv2_imshow(thresholded_image)

#Contrast stretching of an image
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load in grayscale

# Define the min and max values for contrast stretching
min_pixel = np.min(image)
max_pixel = np.max(image)

# Perform contrast stretching
stretched_image = (image - min_pixel) * (255 / (max_pixel - min_pixel))
stretched_image = np.uint8(stretched_image)

# Save the stretched image
cv2.imwrite('stretched_image.jpg', stretched_image)

# Display the stretched image
cv2_imshow(stretched_image)
