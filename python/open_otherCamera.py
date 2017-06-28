# I will try to open USB camera in Jetson TX2.
# git branch and push origin branch

import sys
import cv2
import time
import numpy as np
def read_cam():

    cap = cv2.VideoCapture(1);
    #set image width.
    cap.set(3,1280)
    #set image height.
    cap.set(4,720);
    
    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            start = time.time();
            #cap.read() will return a tuple, flag and image.		
            ret_val,img = cap.read();
	    cv2.imshow('demo',img)
	    #Converter RGB image to grayscale image.
	    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	    #Sobel operation.
	    sobelx = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize=5)
	    cv2.imshow('sobelx',sobelx)
            cv2.waitKey(10)
            end=time.time();
            print (1/(end-start))
    else:
     print "camera open failed"

    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_cam()
