import sys
import time as SYSTIME
import Adafruit_DHT


# Parse command line parameters.
sensor = Adafruit_DHT.AM2302
pin = 4

def getData():
	humperc, tempC = Adafruit_DHT.read_retry(sensor, pin)
	tempF = ((tempC * 1.8) + 32)
	date = SYSTIME.strftime("%m/%d/%y")
	time = SYSTIME.strftime("%H:%M:%S")
	data = [date, time, tempC, tempF, humperc]
	return data
