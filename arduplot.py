# Arduboom - vp1147 @ Jan 10th, 2021
# ArduPlot - vp1147 @ Jun 23rd, 2022

import serial
import time, getch # import external libs
import tg # Teenygraph lib. See README.md

# Search for the Arduino-connected port
try: port = serial.Serial("/dev/ttyUSB0")
except:
    try: port = serial.Serial("/dev/ttyUSB1")
    except: 
    	try: port = serial.Serial("/dev/ttyUSB2")
    	except: 
    		print("No Arduino detected to USB ports.\n")
    		print("Please make sure your Arduino is connected and working")
List = {}

# Number of samples per cycle
samples = 1000

# Start tg
tg.theme("dark.json")
tg.init(800, samples, 100)

# Get the samples
def SerialGet(x):
	return int(serial.Serial.readline(port))

while 1:
	try:
		tg.plot(SerialGet)
	tg.clear()

# # Loop cycle
# while 1:
#     for i in range(0, samples): 
#         #print(int(serial.Serial.readline(port)))
#         List[i] = int(serial.Serial.readline(port))
#         time.sleep(5/1000)
    
#     List = {}