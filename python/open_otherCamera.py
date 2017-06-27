# I will try to open USB camera in Jetson TX2.
# git branch and push origin branch

import sys
import cv2
import time
def read_cam():

    cap = cv2.VideoCapture(1);
    cap.set(3,1920);
    cap.set(4,1080);
    
    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            start = time.time();
            ret_val, img = cap.read();
	    cv2.imshow('demo',img)
	    '''img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    cv2.imshow('demo2',img_gray)'''
            cv2.waitKey(10)
            end=time.time();
            print (1/(end-start))
    else:
     print "camera open failed"

    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_cam()
