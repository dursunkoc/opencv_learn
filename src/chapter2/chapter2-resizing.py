import cv2

img = cv2.imread('data/images/lambo.png')
print(img.shape)
imgResized = cv2.resize(img, (1246, 924))
cv2.imshow("Original Lambo",img)
cv2.imshow("Enlarged Lambo",imgResized)

cv2.waitKey(0)