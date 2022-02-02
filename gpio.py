import RPi.GPIO as GPIO
from dbFunctions import *

def configGPIO() :
    GPIO.setmode(GPIO.BCM)
    
    # Input 23 - input for energy counter
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def pin14callback(channel):
        addPulsesToEnergyCounter()
    
    GPIO.add_event_detect(14, GPIO.RISING, callback=pin14callback, bouncetime=500)
    