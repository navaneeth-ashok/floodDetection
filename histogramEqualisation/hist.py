import numpy as np
import cv2

im = cv2.imread('abc.jpg')
img_hist_equalized = cv2.cvtColor(im,cv2.COLOR_BGR2YCrCb)
y,cr,cb = cv2.split(img_hist_equalized)
equ = cv2.equalizeHist(y)
img = cv2.merge((equ,cr,cb))
img_hist_equalized = cv2.cvtColor(img,cv2.COLOR_YCrCb2BGR)
cv2.imshow('orig',im)
cv2.imshow('equalized',img_hist_equalized)
cv2.imwrite('orig.jpg',im)
cv2.imwrite('equalized.jpg',img_hist_equalized)
