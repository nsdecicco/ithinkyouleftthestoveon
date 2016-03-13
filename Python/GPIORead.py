#!/usr/bin/python
import mraa     # For accessing the GPIO
import time     # For sleeping between blinks
"""
This script demonstrates the usage of mraa library for controlling a 
GPIO as output
setup:
The LED is connected port D5
Demo:
start the application in the command line by using following command:
python blink.py
You should see LED blink 
You can exit this demo by hitting ctrl+c
Link for this tutorial:
https://navinbhaskar.wordpress.com/2015/03/20/python-on-intel-galileoedison-part-1/
"""
LED_GPIO = 4                   # we are using D5 pin
blinkLed = mraa.Gpio(LED_GPIO) # Get the LED pin object
blinkLed.dir(mraa.DIR_IN)      # Set the direction as output

# One infinite loop coming up
while True:
    if blinkLed == 0:
        #Sensor is engaged
        print 'engaged'
    else:
		#Sensor is not engaged
        print 'YOU LEFT THE STOVE ON'
         
    time.sleep(1)
