#!/usr/bin/python
import mraa     # For accessing the GPIO
import time     # For sleeping between reading the Input
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
GPIO_In = 4                   # we are using D4 pin
Input_GPIO = mraa.Gpio(GPIO_In) # Get the Input pin object
Input_GPIO.dir(mraa.DIR_IN)      # Set the direction as Input

# One infinite loop coming up
while True:
    if Input_GPIO.read() == 0:
        #Sensor is engaged
        print 'engaged! You may continue.'
    else:
		#Sensor is not engaged
        print 'YOU LEFT THE STOVE ON!!!'
         
    time.sleep(1)
