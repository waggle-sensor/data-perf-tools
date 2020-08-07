import argparse
import time
from threading import Thread
from queue import Queue
import cv2


# URL = 'rtsp://10.0.0.155/nph-h264.cgi'
# URL = 'http://10.0.0.155/nph-h264.cgi'
URL = 'http://10.0.0.155/nph-mjpeg.cgi'


def run_worker(id, q):
    while True:
        cap = cv2.VideoCapture(URL)
        if cap.isOpened():
            break
        cap.close()
        time.sleep(1)

    # wait for first frame
    while True:
        ok, _ = cap.read()
        if ok:
            break

    start = time.monotonic_ns()

    while True:
        ok, _ = cap.read()

        if ok:
            q.put((id, time.monotonic_ns() - start))


def get_stream_resolution():
    cap = cv2.VideoCapture(URL)

    while True:
        ok, frame = cap.read()
        if ok:
            h, w, d = frame.shape
            return f'{w}x{h}x{d}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()

    q = Queue()

    # resolution = get_stream_resolution()

    for i in range(args.n):
        t = Thread(target=run_worker, args=(i, q), daemon=True)
        t.start()

    print('id,timestamp')

    while True:
        print(*q.get(), sep=',')


if __name__ == '__main__':
    main()
