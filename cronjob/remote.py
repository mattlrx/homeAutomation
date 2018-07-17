import RPi.GPIO as GPIO ## Import GPIO library
import time
import sys

def setup():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(38, GPIO.OUT)
## Setup GPIO Pin 7 to OUT
    GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

def switchIt(pinNumber):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(pinNumber, GPIO.OUT) ## Setup GPIO Pin pinNumber to OUT
    GPIO.output(pinNumber,False)
    time.sleep(2)
    GPIO.output(pinNumber,True) 
    GPIO.cleanup()

def gardenLightOn():
    switchIt(40)

def gardenLightOff():
    switchIt(38)

def livingLightOn():
    switchIt(37)

def livingLightOff():
    switchIt(35)

# testremote.py can be called directly with the pin number.
if str(sys.argv[1]).isdigit() :
    switchIt(int(sys.argv[1]))
elif str(sys.argv[1]) == 'gardenLightOn':
    gardenLightOn()
elif str(sys.argv[1]) == 'allLightsOn':
    livingLightOn()
    gardenLightOn()
elif str(sys.argv[1]) == 'gardenLightOff':
    gardenLightOff()
elif str(sys.argv[1]) == 'livingLightOn':
    livingLightOn()
elif str(sys.argv[1]) == 'livingLightOff':
    livingLightOff()
