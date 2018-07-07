import RPi.GPIO as GPIO ## Import GPIO library
import time

def setup():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(38, GPIO.OUT)
## Setup GPIO Pin 7 to OUT
    GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 7 to OUT


def lightOn():

##GPIO.setup(31, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
##GPIO.output(37,True) ## Turn on GPIO pin 7
    GPIO.output(40,False) ## Turn on GPIO pin 7
    time.sleep(2)
    GPIO.output(40,True) ## Turn on GPIO pin 7
    GPIO.cleanup()

def lightOff():
    GPIO.output(38,False)
    time.sleep(2)
    GPIO.output(38,True) 
    GPIO.cleanup()

def switchIt(pinNumber):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(pinNumber, GPIO.OUT) ## Setup GPIO Pin pinNumber to OUT
    GPIO.output(pinNumber,False)
    time.sleep(2)
    GPIO.output(pinNumber,True) 
    GPIO.cleanup()
