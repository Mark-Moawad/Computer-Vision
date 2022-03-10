import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResized = cv2.resize(img, (300, 200))
print(imgResized.shape)

imgStretched = cv2.resize(img, (1000, 500))
print(imgStretched.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResized)
cv2.imshow("Stretched Image", imgStretched)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
