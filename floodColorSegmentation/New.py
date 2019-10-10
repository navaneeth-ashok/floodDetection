import numpy as np
import cv2
 
img = cv2.imread('abc.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
     # define range of blue color in HSV, ([B,G,R])
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
    
        # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
        # Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
    
cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('abcgray.png',img)
    cv2.destroyAllWindows()

#k = cv2.waitKey(5) & 0xFF
    
#cv2.destroyAllWindows()
