import argparse
import time
from threading import Thread
from queue import Queue
import cv2


def run_worker(url, id, q):
    while True:
        cap = cv2.VideoCapture(url)
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


def get_stream_resolution(url):
    cap = cv2.VideoCapture(url)

    while True:
        ok, frame = cap.read()
        if ok:
            h, w, d = frame.shape
            return f'{w}x{h}x{d}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('n', type=int)
    args = parser.parse_args()

    rates = [0] * args.n

    q = Queue()

    resolution = get_stream_resolution(args.url)

    for i in range(args.n):
        t = Thread(target=run_worker, args=(args.url, i, q), daemon=True)
        t.start()

    while True:
        id, rate = q.get()
        rates[id] = round(rate, 3)
        print(args.url, resolution, *rates, sep='\t')


if __name__ == '__main__':
    main()
