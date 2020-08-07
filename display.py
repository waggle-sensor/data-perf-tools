import cv2
import numpy as np
import time
from threading import Thread
from queue import Queue

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name

# URL = 'rtsp://10.0.0.155/nph-h264.cgi'
# URL = 'http://10.0.0.155/nph-h264.cgi'
URL = 'http://10.0.0.155/nph-mjpeg.cgi'

cap = cv2.VideoCapture(URL)

# Check if camera opened successfully
if cap.isOpened() is False:
    print("Error opening video stream or file")

# Read until video is completed
total = 0
start = time.monotonic()

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    total += 1
    print(total / (time.monotonic() - start), frame.shape)
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
