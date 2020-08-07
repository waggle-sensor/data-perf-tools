import argparse
import time
from threading import Thread
from queue import Queue
import cv2


#URL = 'rtsp://10.0.0.155/nph-h264.cgi'
#URL = 'http://10.0.0.155/nph-h264.cgi'
URL = 'http://10.0.0.155/nph-mjpeg.cgi'


def run_worker(id, q):
    while True:
        cap = cv2.VideoCapture(URL)
        if cap.isOpened():
            break
        cap.close()
        time.sleep(1)

    batch_size = 60

    while True:
        total = 0
        start = time.monotonic()
        while total < batch_size:
            ok, _ = cap.read()
            if ok:
                total += 1
        rate = batch_size / (time.monotonic() - start)
        q.put((id, rate))


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

    rates = [0] * args.n

    q = Queue()

    resolution = get_stream_resolution()

    for i in range(args.n):
        t = Thread(target=run_worker, args=(i, q), daemon=True)
        t.start()

    while True:
        id, rate = q.get()
        rates[id] = round(rate, 3)
        print(URL, resolution, *rates, sep='\t')


if __name__ == '__main__':
    main()
