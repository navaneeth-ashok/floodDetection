import numpy as np
import cv2
abc = np.zeros((1024,768,3), np.uint8)
im = cv2.imread('abc1mask.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
'''cnt = contours[3]
cv2.drawContours(abc, [cnt], 0, (0,255,0), 3)
M = cv2.moments(cnt)
print M'''
abc = 1
for cnt in contours:
	cv2.drawContours(abc,[cnt],-1,(0,255,0), 3)
	cv2.imshow('trial',abc)
	area = cv2.contourArea(cnt)
	print area
	print "contour =" + str(abc)
	abc = abc + 1 
	cv2.waitKey(0)
	
cv2.imshow('imggr',thresh)
cv2.imshow('frame',im2)
cv2.waitKey(0)
cv2.imwrite('contour_result.jpg',im2)
