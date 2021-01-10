import serial,time

try: port = serial.Serial("/dev/ttyUSB0")
except:
    try: port = serial.Serial("/dev/ttyUSB1")
    except: port = serial.Serial("/dev/ttyUSB2")

List = {}
while 1:
    for i in range(0, 300):
        #print(int(serial.Serial.readline(port)))
        List[i] = int(serial.Serial.readline(port))
        time.sleep(5/1000)
    print(List)
    List = {}