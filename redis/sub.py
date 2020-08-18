from redis import Redis
import time
import struct
from base64 import b64decode

r = Redis()

batch_size = 100

s = r.pubsub()
s.subscribe("data")

print(s.get_message(timeout=10.0))

while True:
    start = time.monotonic()
    max_delay_ms = 0.0
    for _ in range(batch_size):
        data = b64decode(s.get_message(timeout=10.0)['data'])
        now = time.time_ns()
        send_time, = struct.unpack_from('Q', data)
        delay_ms = (now - send_time) / 10e6
        max_delay_ms = max(max_delay_ms, delay_ms)
    print(now, batch_size / (time.monotonic() - start), max_delay_ms, flush=True)
