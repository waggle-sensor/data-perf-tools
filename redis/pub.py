from redis import Redis
import time
import struct
from base64 import b64encode

r = Redis()

# data = bytes(640*480*3)
data = bytes(1024**2)

while True:
    print(time.time_ns())
    r.publish("data", b64encode(struct.pack('Q', time.time_ns()) + data))
    time.sleep(1/100)
