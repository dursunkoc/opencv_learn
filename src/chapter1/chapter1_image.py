import cv2
import os

img = cv2.imread("data/images/lena.png")
print(os.getcwd())
print(img)

cv2.imshow("Output-1", img)

cv2.waitKey(0)