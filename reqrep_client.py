import zmq
import time 
from sense_emu import SenseHat
import json

from zmq.sugar.frame import Message 
port="5546"
context = zmq.Context(1)
socket=context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)
sense=SenseHat()
obj=dict()
while True:
    obj['tempreture']=sense.temp
    obj['Humidity']=sense.humidity
    obj["pressure"]=sense.pressure
    socket.send_json(obj)
    time.sleep(1)
    message=socket.recv_string()
    print(message)
    
    