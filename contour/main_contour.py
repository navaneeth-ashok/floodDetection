import numpy as np
import cv2
from glob import glob
import time



i=1

img_mask1 = '/home/wanderer/Project/Water/*.jpg'
img_names = glob(img_mask1)
print('processing...')

for fn in img_names:
	print('processing %s...' % fn,)
	im = cv2.imread(fn)
	im2 = cv2.imread(fn)
	abc = np.zeros((1024,768,3), np.uint8)
	height, width, channels = im.shape
	size = height * width
	
	
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	im2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
	num = 0
	largest_area = 0
	count = 0
	
	for cnt in contours:
		cv2.drawContours(im2,[cnt],-1,(0,255,0), 3)
		#cv2.imshow('trial',abc)
		area = cv2.contourArea(cnt)
		
		if area > largest_area:
			largest_area = area
			count  = num
		num = num + 1		
	
	amount =  (largest_area / size) * 100
	round_per = float("{0:.2f}".format(amount)) 
			
	print "Largest area   = " + str(largest_area)
	print "Contour Number = " + str(count)
	print "Size = " + str(size) 
	print "Percentage = " + str(amount)
	cnt = contours[count]
	cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
	#cv2.imwrite('contour_result_new.jpg',overlap)
	##########
	cv2.putText(im, "Perc ={}".format(round_per), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	'''cv2.putText(im, "{}".format(width), (10, 55),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.putText(im, " * {}".format(height), (60, 55),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.putText(im, " = {}".format(size), (120, 55),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.putText(im, "Contour={}".format(largest_area), (10, 75),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)'''		
	##########	
	cv2.imwrite('/home/wanderer/Project/ContourResult/thresh_' + str(i) +'.jpg',im) 
	
	i = i + 1
