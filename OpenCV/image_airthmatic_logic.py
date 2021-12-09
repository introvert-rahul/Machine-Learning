import numpy as np
import cv2
img1 = cv2.imread('/home/g-host/Documents/OpenCV for python(Img and video analysis)/pic2.jpg')
img2 = cv2.imread('/home/g-host/Documents/OpenCV for python(Img and video analysis)/pic1.jpg')

add = img1  +  img2
cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()

