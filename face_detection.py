
# Code 8: Face Detection using OpenCV and Haar Cascade

# Install required libraries in the VS Code terminal:
# python -m pip install opencv-python
# python -m pip install matplotlib

# Import libraries
import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("image.png")

# Load Haar Cascade classifier
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# Detect faces
faces = faceCascade.detectMultiScale(gray)

print("Found {} faces!".format(len(faces)))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display image with detected faces
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()