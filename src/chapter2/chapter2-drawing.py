import cv2
import numpy as np

img = np.zeros((300,500,3))
img[100:110]=(0,0,255)
img[:,100:110]=(0,0,255)
cv2.line(img,(0,0),(250, 150), (0,255,0),3)
cv2.rectangle(img,(0,0),(50, 30), (0,0,255),2)
cv2.circle(img,(250,50),10,(255,255,0),1)

cv2.putText(img,"Open CV", (300,100), cv2.FONT_ITALIC, 1, (0,150,0),1)

cv2.imshow("Canvas", img)



cv2.waitKey(0)