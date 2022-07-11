# Arduboom - vp1147 @ Jan 10th, 2021
# ArduPlot v1.0 - vp1147 @ Jun 23rd, 2022

import serial
import time, getch 			# import external libs
import tg 					# Teenygraph lib. See README.md

OnTermValues = False 		# Set to True for printing only text results

# Search for the Arduino-connected port
try: port = serial.Serial("/dev/ttyUSB0")
except:
    try: port = serial.Serial("/dev/ttyUSB1")
    except: 
    	try: port = serial.Serial("/dev/ttyUSB2")
    	except: 
    		print("No Arduino detected on USB ports.")
    		print("Please make sure your Arduino is connected and working")
List = {}

# Number of samples per cycle
samples = 300

# Start tg
if OnTermValues == False:
	tg.theme("dark.json")
	tg.init(800, samples, samples/10)

# Get the samples
def SerialGet(x):
	return int(serial.Serial.readline(port))

if OnTermValues == False:
	while 1:
		print(tg.plot(SerialGet))
		tg.clear()
else:
	while 1: print(SerialGet(0))
# # Loop cycle
# while 1:
#     for i in range(0, samples): 
#         #print(int(serial.Serial.readline(port)))
#         List[i] = int(serial.Serial.readline(port))
#         time.sleep(5/1000)
    
#     List = {}