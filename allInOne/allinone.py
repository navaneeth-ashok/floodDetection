import numpy as np
import cv2
from glob import glob

#face_cascade = cv2.CascadeClassifier('/home/nikhitha/OpenCV/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_alt.xml')
face_cascade1 = cv2.CascadeClassifier('/home/wanderer/OpenCV/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_alt.xml')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

i=1

img_mask1 = '/home/wanderer/Project/Input/*.jpg'
img_names = glob(img_mask1)
print('processing...')

for fn in img_names:
	print('processing %s...' % fn,)
	img = cv2.imread(fn)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_brown = np.array([0,0,0])
	upper_brown = np.array([45,255,255])
	
	mask = cv2.inRange(hsv, lower_brown, upper_brown) 
	cv2.imwrite('/home/wanderer/Project/mask' + str(i) +'.jpg',img) 
	
	res = cv2.bitwise_and(img,img, mask= mask)
	cv2.imwrite('/home/wanderer/Project/res/' + str(i) +'.jpg',img)

	faces = face_cascade1.detectMultiScale(res,scaleFactor=1.015,minNeighbors=3,minSize=(3, 3),flags = cv2.CASCADE_SCALE_IMAGE)
	for (x,y,w,h) in faces:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,127),2)
		roi_res = res[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	cv2.imwrite('/home/wanderer/Project/Output/' + str(i) +'.jpg',img)
	
	image = imutils.resize(img, width=min(400, img.shape[1]))
	orig = image.copy()
	 
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
	padding=(8, 8), scale=1.05)
	 
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
	 
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
	 
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	cv2.imwrite('/home/wanderer/Project/Human/' + str(i) +'.jpg',img)
	i = i + 1
