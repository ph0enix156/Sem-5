"""
================================================================================
FACE DETECTION USING OPENCV AND HAAR CASCADE CLASSIFIER
================================================================================

PREREQUISITES:
1. Python 3.x installed.
2. Required Third-Party Libraries:
   - opencv-python: Computer vision library for image processing & face detection.
   - matplotlib: Visualization library used to display images.

HOW TO INSTALL DEPENDENCIES:
  Run in terminal / PowerShell:
      pip install opencv-python matplotlib

  Or using python module flag:
      python -m pip install opencv-python matplotlib

ASSETS REQUIRED IN PROJECT FOLDER:
  1. An image file (e.g., 'image.png' or 'image.jpg') containing human face(s).
  2. The pre-trained Haar Cascade XML model:
     'haarcascade_frontalface_default.xml'
     (If not present in current directory, OpenCV's built-in model path is used as fallback).

HOW TO RUN:
  Open terminal in this directory and execute:
      python face_detection.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
import os
import cv2                                     # OpenCV library for computer vision
import matplotlib.pyplot as plt                 # Matplotlib for rendering images


# ==============================================================================
# SECTION 2: LOAD IMAGE & HAAR CASCADE MODEL
# ==============================================================================
IMAGE_PATH = "image.png"

# Read image from disk (OpenCV loads images in BGR format by default)
image = cv2.imread(IMAGE_PATH)

# Verify if the image was successfully loaded
if image is None:
    print(f"Error: Image '{IMAGE_PATH}' not found! Place an 'image.png' in this directory.")
    exit()

# Model filename
cascade_path = "haarcascade_frontalface_default.xml"

# Fallback: if local xml doesn't exist, use OpenCV's built-in cascade directory
if not os.path.exists(cascade_path):
    cascade_path = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")

# Load pre-trained Haar Cascade Classifier for frontal face detection
faceCascade = cv2.CascadeClassifier(cascade_path)


# ==============================================================================
# SECTION 3: PREPROCESSING - CONVERT TO GRAYSCALE
# ==============================================================================
# Face detection algorithms work on luminance (intensity) rather than color.
# Grayscale conversion reduces data from 3 channels (B, G, R) to 1, speeding up processing.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display original RGB image using matplotlib (convert BGR -> RGB for correct colors)
plt.figure("Original Image")
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()


# ==============================================================================
# SECTION 4: DETECT FACES (MULTI-SCALE DETECTION)
# ==============================================================================
# detectMultiScale scans the image across multiple scales to detect faces of varying sizes.
# Parameters:
#   gray: Grayscale input image.
#   scaleFactor: Compensates for faces appearing larger/smaller closer to camera (default ~1.1).
#   minNeighbors: How many neighbors each candidate rectangle should have to retain it.
# Returns: List of bounding boxes: [(x, y, width, height), ...]
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print(f"Found {len(faces)} face(s)!")


# ==============================================================================
# SECTION 5: DRAW BOUNDING BOXES & DISPLAY RESULT
# ==============================================================================
# Draw a rectangle around each detected face on the original color image
# Arguments: (target_image, top_left_corner, bottom_right_corner, color_in_BGR, line_thickness)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # (0, 255, 0) is Green

# Display output image with green bounding boxes
plt.figure("Detected Faces")
plt.title(f"Face Detection Result: {len(faces)} face(s) found")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
