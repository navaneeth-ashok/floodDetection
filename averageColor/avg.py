import numpy as np
import cv2

im = cv2.imread('abc1res.jpg')
mask = np.zeros(im.shape,np.uint8)
mean_val = cv2.mean(mask,mask = mask)
cv2.imshow('mask',mask)
cv2.imshow('image',image)
print "average = " + str(mean_val)
