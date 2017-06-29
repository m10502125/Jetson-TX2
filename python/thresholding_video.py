# Open USB camera in Jetson TX2.
# and thresholding the input video frame.

import sys
import cv2
import time
import numpy as np

def read_cam():

    cap = cv2.VideoCapture(1);
    #set image width.
    cap.set(3,640)
    #set image height.
    cap.set(4,480);
    
    if cap.isOpened():
         while True:
            start = time.time();
            #cap.read() will return a tuple, flag and image.		
            ret_val,img = cap.read();
	    #Converter RGB image to grayscale image.
	    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	    cv2.imshow('gray image',img_gray)
	    #blur the gray image
	    img_blur = cv2.medianBlur(img_gray,5)
	    #simple thresholding
	    ret,th1 = cv2.threshold(img_blur,127,255,cv2.THRESH_BINARY)	    
            cv2.imshow('blur + simple threshold',th1)
            #adaptive threshold
            adap_th = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
	    cv2.imshow('adap_th',adap_th)
            cv2.waitKey(10)
            end=time.time();
            print (1/(end-start))
    else:
     print "camera open failed"

if __name__ == '__main__':
    read_cam()
