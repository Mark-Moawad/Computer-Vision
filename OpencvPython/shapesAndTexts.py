import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# to color the whole image
img[:] = 255, 0, 0

# to color a specific region of the image
# img[200:300, 100:300] = 255, 0, 0

# to draw a line in a specific region
# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)

# reset image to black
img[:] = 0, 0, 0

# to draw a line from corner to corner
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# to draw a rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# to draw a filled rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# to draw a circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# to add text to an image
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 150, 200), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)
