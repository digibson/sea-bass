#!/usr/bin/env python3.4
#should check the above line for latest version
# need to run sudo apt-get install python-rpi.gpio python3-rpi.gpio
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
#Initialise pin 21 with pullup  
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# Wait for falling edge 
try:  
    GPIO.wait_for_edge(21, GPIO.FALLING)  
    print("Button pressed /n")  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit
