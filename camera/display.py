import argparse
import cv2
import numpy as np
import time
from threading import Thread
from queue import Queue


def stream_images(url, q):
    while True:
        cap = cv2.VideoCapture(url)
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
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()

    q = Queue()
    t = Thread(target=stream_images, args=(args.url, q), daemon=True)
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
