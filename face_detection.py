
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("2.png")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

faces = faceCascade.detectMultiScale(gray)

print("Found {} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
