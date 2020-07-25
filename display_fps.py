import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

count = 0

time_start = time.time()
while True:
    ret, frame = cap.read()
    # cv2.imshow('window', frame)
    # cv2.waitKey(1)
    count += 1

    if(count%30==0):
        time_end = time.time()
        time_diff = time_end - time_start
        print(30/time_diff)
        print(frame.shape)
        time_start = time.time()
