import cv2

img = cv2.imread('data/images/lambo.png')

imgCropped = img[0:200, 200:500]
cv2.imshow("Original Lambo",img)
cv2.imshow("Cropped Lambo",imgCropped)

cv2.waitKey(0)