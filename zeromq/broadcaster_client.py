import zmq
import time
import struct

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://localhost:5556')

socket.setsockopt_string(zmq.SUBSCRIBE, '')

batch_size = 100

while True:
    start = time.monotonic()
    max_delay_ms = 0.0
    for _ in range(batch_size):
        data = socket.recv()
        send_time, = struct.unpack_from('Q', data)
        now = time.time_ns()
        delay_ms = (now - send_time) / 10e6
        max_delay_ms = max(max_delay_ms, delay_ms)
    print(now, batch_size / (time.monotonic() - start), max_delay_ms, flush=True)
