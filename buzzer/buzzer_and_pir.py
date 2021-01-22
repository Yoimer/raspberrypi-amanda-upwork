# pins configuration (pir)
# jumper on pir has to be on H
# pir red ----> 2 RPI (5V)
# pir brown ----> GPIO(17) 11
# pir black ----> 39 RPI (GND)

# pins configuration (buzzer)
# positive on buzzer     GPIO(27) 27 on pi
# negative on buzzer     GPIO(39) on pi (GND)

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# for GPIO numbering, choose BCM  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(17, GPIO.IN)                 #Read output from PIR motion sensor
GPIO.setup(2, GPIO.OUT)                 #LED output pin
GPIO.setup(27, GPIO.OUT)                #Set buzzer - pin 27 (27) as output

def triggerbuffer():
    #beeping
    GPIO.output(27, GPIO.HIGH)
    print ("Beeping")
    time.sleep(0.5)
    #no beeping
    GPIO.output(27, GPIO.LOW)
    print ("No Beep")
    time.sleep(0.5)


while True:
    i=GPIO.input(17)
    if i == 0:                             #When output from motion sensor is LOW
        print("No intruders",i)
        GPIO.output(2, GPIO.LOW)          #Turn OFF LED
        time.sleep(0.1)                      # Delay in seconds
        #no beeping
        #GPIO.output(27, 0)
        GPIO.output(27, GPIO.LOW)
    elif i == 1:                           #When output from motion sensor is HIGH
        while (GPIO.input(17) == 1):
            print("Intruder detected",i)
            GPIO.output(2, GPIO.HIGH)      #Turn ON LED
            time.sleep(0.1)
            triggerbuffer();