#Low Pass Filtering
import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path)

# Apply a Gaussian blur (low pass filter)
kernel_size = (5, 5)  # Size of the kernel
low_pass_filtered_image = cv2.GaussianBlur(image, kernel_size, sigmaX=0)

# Save the filtered image
cv2.imwrite('low_pass_filtered_image.jpg', low_pass_filtered_image)

# Display the filtered image
cv2_imshow(low_pass_filtered_image)


#High Pass Filtering
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path)

# Apply a Gaussian blur (low pass filter)
kernel_size = (5, 5)
blurred_image = cv2.GaussianBlur(image, kernel_size, sigmaX=0)

# Subtract the blurred image from the original image to get the high pass filtered image
high_pass_filtered_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)

# Save the filtered image
cv2.imwrite('high_pass_filtered_image.jpg', high_pass_filtered_image)

# Display the filtered image
cv2_imshow(high_pass_filtered_image)

#Median Filtering
import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/mr.bean.jpg'
image = cv2.imread(image_path)

# Apply median filtering
median_filtered_image = cv2.medianBlur(image, ksize=5)  # ksize must be an odd integer

# Save the filtered image
cv2.imwrite('median_filtered_image.jpg', median_filtered_image)

# Display the filtered image
cv2_imshow(median_filtered_image)

