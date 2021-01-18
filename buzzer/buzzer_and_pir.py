# pins configuration (pir)
# jumper on pir has to be on H
# pir red ----> 2 RPI (5V)
# pir brown ----> GPIO(17) 11
# pir black ----> 39 RPI (GND)

# pins configuration (buzzer)
# positive on buzzer     GPIO(27) 13 on pi
# negative on buzzer     GPIO(39) on pi (GND)

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)                 #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)                 #LED output pin
GPIO.setup(13, GPIO.OUT)                #Set buzzer - pin 27 (13) as output

def triggerbuffer():
    #beeping
    GPIO.output(13, 1)
    print ("Beeping")
    time.sleep(0.5)
    #no beeping
    GPIO.output(13, 0)
    #print ("No Beep")
    time.sleep(0.5)


while True:
    i=GPIO.input(11)
    if i == 0:                             #When output from motion sensor is LOW
        print("No intruders",i)
        GPIO.output(3, 0)                #Turn OFF LED
        time.sleep(0.1)                      # Delay in seconds
        #no beeping
        GPIO.output(13, 0)

    elif i == 1:                           #When output from motion sensor is HIGH
        while (GPIO.input(11) == 1):
            print("Intruder detected",i)
            GPIO.output(3, 1)                #Turn ON LED
            time.sleep(0.1)
            triggerbuffer();