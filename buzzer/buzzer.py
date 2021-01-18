# wiring
# https://projects.raspberrypi.org/en/projects/physical-computing/8

from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(27)

while True:
    print("Buzzer is ON")
    buzzer.on()
    sleep(1)
    buzzer.off()
    print("Buzzer is OFF")
    sleep(1)