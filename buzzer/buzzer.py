# wiring
# https://projects.raspberrypi.org/en/projects/physical-computing/8

#Libraries
import RPi.GPIO as GPIO
from time import sleep

#Disable warnings (optional)
GPIO.setwarnings(False)

#Select GPIO mode
GPIO.setmode(GPIO.BOARD)

#Set buzzer - pin 27 as output
buzzer = 13
GPIO.setup(buzzer,GPIO.OUT)

#Run forever loop
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beeping")
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beeping")
    sleep(0.5)