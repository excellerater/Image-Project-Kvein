import cv2
import numpy as np

# 简单的mask获取方法

src = cv2.imread('moon.jpg')
cv2.imshow('src', src)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (11, 43, 46), (25, 255, 255))

# mask = cv2.bitwise_not(mask)
print(mask)
cv2.imwrite('moon-mask.jpg', mask)
cv2.imshow('mask', mask)
cv2.waitKey(0)