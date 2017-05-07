#!/usr/bin/env python3.6
# Need to confirm the above.  Both buttons should be pulled high by code (or with hardware) 
  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 & 24 set up as inputs. One pulled up, the other down.  
# 23 will go to GND when button pressed and 24 will go to 3V3 (3.3V)  
# this enables us to demonstrate both rising and falling edge detection  
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# threaded callback function  
def take_picture(channel):  
    print("Shutter release.")
  
  
# The GPIO.add_event_detect() line below set things up so that  
# when a rising edge is detected on port 24, regardless of whatever   
# else is happening in the program, the function "my_callback" will be run  
# It will happen even while the program is waiting for  
# a falling edge on the other button.  
GPIO.add_event_detect(24, GPIO.FALLING, callback=take_picture)  
  
try:  
    print "Waiting for falling edge on port 23"  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    print("Shutdown function.")  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
