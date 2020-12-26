import cv2
import numpy as np

img = cv2.imread("data/images/lena.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img, 250, 400)

kernel = np.ones((4,4))
imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilated, kernel, iterations=1)



#cv2.imshow("Gray Scale",imgGray)
#cv2.imshow("Blur Scale",imgBlur)

cv2.imshow("Canny Scale",imgCanny)
cv2.imshow("Dilated Scale",imgDilated)
cv2.imshow("Eroded Scale",imgEroded)

cv2.waitKey(0)
