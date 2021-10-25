import zmq
import time 

port="5546"
context = zmq.Context()
socket=context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    message=socket.recv_string()
    print(message)
    time.sleep(1)
    send="got it"
    socket.send_string(send)
