# ArduPlot - vp1147 @ Jan 10th, 2021
# Receives data from an device connected to 
# the USB serial port (i.e. Arduino) and plots
# it in function of time. Useful for sensor 
# analysis and current measurements.

## Dependencies: pyserial , getch , time

import serial, math
import time, getch 			# import external libs
import tg 					# Teenygraph lib. See README.md

OnTermValues = False 		# Set to True for printing only text results

def PortSearch():
	port = serial.Serial("/dev/ttyACM0")
	return port
	print("Arduino is connected on",port)

samples = 800				# Number of samples per cycle
factor = 10
subdiv = 5
port = PortSearch()			# Search for the Arduino-connected port

# Start tg
if OnTermValues == False:
	tg.theme("dark.json")
	tg.init(800, samples * factor, int( samples / subdiv * factor))

# Get the samples
def SerialGet(x):
	return int(serial.Serial.readline(port))

if port != None:
	if OnTermValues == False:
		while 1:
			tg.plot(SerialGet)
			tg.clear()
	else:
		while 1: print(SerialGet(0))
