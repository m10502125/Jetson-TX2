# I will try to open USB camera in Jetson TX2.
# git branch and push origin branch

import sys
import cv2

def read_cam():

    cap = cv2.VideoCapture(0);
    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, img = cap.read();
	    cv2.imshow('demo',img)
	    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    cv2.imshow('demo2',img_gray)
            cv2.waitKey(10)
    else:
     print "camera open failed"

    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_cam()
