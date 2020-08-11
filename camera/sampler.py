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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('n', type=int)
    args = parser.parse_args()

    q = Queue()

    for i in range(args.n):
        t = Thread(target=run_worker, args=(args.url, i, q), daemon=True)
        t.start()

    print('id,timestamp')

    while True:
        print(*q.get(), sep=',')


if __name__ == '__main__':
    main()
