import zmq
import time
import struct

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:5556')

data = bytes(640*480*3)

while True:
    socket.send(struct.pack('Q', time.time_ns()) + data)
    time.sleep(1/100)
