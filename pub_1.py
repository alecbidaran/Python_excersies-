import zmq 
from sense_emu import SenseHat
import time 
port="5555"
context=zmq.Context()
socket=context.socket(zmq.PUB)
host="tcp://"+str(port)+":"
socket.bind("tcp://*:%s" % port)
print("publishing")
sense=SenseHat()
print("==================================")
while True:
    temp=sense.temp
    hum=sense.humidity
    topic="tempreture"
    js=dict()
    js['tempreture']=temp
    js['humidity']=hum
    #message=topic+":"+payload
    print("sending",js)
    socket.send_string("sensors",flags=zmq.SNDMORE)
    socket.send_json(js)
    time.sleep(1)
