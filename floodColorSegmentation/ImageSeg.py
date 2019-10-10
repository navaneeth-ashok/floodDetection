import numpy as np
import cv2
 
img = cv2.imread('abcgamma3.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
     
lower_brown = np.array([0,0,0])
upper_brown = np.array([30,255,255])
    
       
mask = cv2.inRange(hsv, lower_brown, upper_brown)
    
        
res = cv2.bitwise_and(img,img, mask= mask)
    
cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(0)
if k == 27:         # ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # 's' key to save and exit
    cv2.imwrite('abc1mask.png',mask)
    cv2.imwrite('abc1res.png',res)
    cv2.destroyAllWindows()

#k = cv2.waitKey(5) & 0xFF
    
#cv2.destroyAllWindows()
