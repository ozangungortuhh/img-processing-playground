import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output32.avi',fourcc, 10.0, (1280,720))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the frame
        out.write(frame)

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
