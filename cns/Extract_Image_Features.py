#Color Histogram
import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/content/mr.bean.jpg')

# Convert the image to RGB (OpenCV loads images in BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Calculate the histogram for each color channel
colors = ('r', 'g', 'b')
plt.figure(figsize=(10, 5))
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.title('Color Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

#HOG (Histogram of Oriented Gradients)
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/content/mr.bean.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate HOG features
hog = cv2.HOGDescriptor()
hog_features = hog.compute(gray_image)

# Reshape the features for visualization (if needed)
hog_features = hog_features.reshape(-1, 1)

# Display the HOG features
plt.plot(hog_features)
plt.title('HOG Features')
plt.show()

#Canny Edge Detection
import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/content/mr.bean.jpg', cv2.IMREAD_GRAYSCALE)

# Perform Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the edges
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection using Canny')
plt.axis('off')
plt.show()

#ORB (Oriented FAST and Rotated BRIEF)
import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/content/mr.bean.jpg', cv2.IMREAD_GRAYSCALE)

# Create an ORB detector object
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = orb.detectAndCompute(image, None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# Display the result
plt.imshow(image_with_keypoints, cmap='gray')
plt.title('ORB Keypoints')
plt.axis('off')
plt.show()

