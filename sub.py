import zmq
import time 

import sys 

port="5555"
context=zmq.Context()
socket=context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)
print("waiting for message")
while True :
    socket.subscribe("sensors")
    string=socket.recv_string()
    obj=socket.recv_json()

    print(obj)