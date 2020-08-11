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


def stream_images(q):
    while True:
        cap = cv2.VideoCapture(URL)
        if cap.isOpened():
            break
        time.sleep(1)

    try:
        while True:
            ok, frame = cap.read()
            if ok:
                q.put(frame)
    finally:
        cap.release()


def main():
    q = Queue()
    t = Thread(target=stream_images, args=(q,), daemon=True)
    t.start()

    try:
        while True:
            frame = q.get()
            cv2.imshow('Frame', frame)
            cv2.waitKey(1)
    finally:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
