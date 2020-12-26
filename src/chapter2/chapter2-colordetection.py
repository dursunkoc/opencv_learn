import cv2
import numpy as np

trackBar = "TrackBars"
hueMin = "Hue Min"
hueMax = "Hue Max"
satMin = "Sat Min"
satMax = "Sat Max"
valMin = "Val Min"
valMax = "Val Max"


def onChanged(key):
    def onKeyChanged(v):
        redrawMask()
    return onKeyChanged

cv2.namedWindow(trackBar)
cv2.resizeWindow(trackBar, 700, 240)
cv2.createTrackbar(hueMin, trackBar, 0, 179, onChanged(hueMin))
cv2.createTrackbar(hueMax, trackBar, 19, 179, onChanged(hueMax))
cv2.createTrackbar(satMin, trackBar, 110, 255, onChanged(satMin))
cv2.createTrackbar(satMax, trackBar, 240, 255, onChanged(satMax))
cv2.createTrackbar(valMin, trackBar, 153, 255, onChanged(valMin))
cv2.createTrackbar(valMax, trackBar, 255, 255, onChanged(valMax))

path = "data/images/lambo.png"
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)

def redrawMask():
    h_min = cv2.getTrackbarPos(hueMin, trackBar)
    h_max = cv2.getTrackbarPos(hueMax, trackBar)
    s_min = cv2.getTrackbarPos(satMin, trackBar)
    s_max = cv2.getTrackbarPos(satMax, trackBar)
    v_min = cv2.getTrackbarPos(valMin, trackBar)
    v_max = cv2.getTrackbarPos(valMax, trackBar)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,(0,180,0),mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

cv2.waitKey(0)