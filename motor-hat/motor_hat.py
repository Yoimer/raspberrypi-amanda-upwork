# Before this code can run, the library named: adafruit-circuitpython-motorkit
# must be installed on your Raspberry Pi. Install it with this command:
# sudo pip3 install adafruit-circuitpython-motorkit

# You'll need the three lines below each time you
# write code to power the bot
from adafruit_motorkit import MotorKit
#kit = MotorKit()
# NOTE: If using the Waveshare Motor Driver Hat, change the above line to:
kit = MotorKit(0x40)
# Also, only if using the Waveshare Motor Driver Hat, be sure you've installed
# and modified CircuitPython files, in particular the file at:
# sudo nano /usr/lib/python3/dist-packages/adafruit_motorkit.py
# as described in the tutorial at:
# https://gallaugher.com/makersnack-install-and-test-the-waveshare-raspberry-pi/
import time

# Forward at full throttle
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
# A 1.0 second sleep pauses the code while
# motors are running. After 1.0 sec., the
# lines after sleep will set throttle to zero,
# effectively turning the motor off.
print("Forward at full throttle")
time.sleep(1.0)
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
print("Stop & sleep for 1 sec.")
time.sleep(1.0)

# Right at half speed
kit.motor1.throttle = 0.5
kit.motor2.throttle = -0.5
# let motors run for 2.0 seconds.
print("Right Motor at half speed")
time.sleep(2.0)
# Stop. Sleep for 3 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
print("Stop. Sleep for 3 sec.")
time.sleep(3.0)

# Backward at 3/4 speed
kit.motor1.throttle = -0.75
kit.motor2.throttle = -0.75
# let motors run for 2.5 seconds
print("Backward at 3/4 speed")
time.sleep(2.5)
# Stop. Sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
print("Stop. Sleep for 1 sec.")
time.sleep(1.0)

# Forward rt at full speed, backward left at 1/4 speed
kit.motor1.throttle = 1.0
kit.motor2.throttle = -0.25
# let motors run for 3 seconds
print("Forward rt at full speed, backward left at 1/4 speed")
time.sleep(3.0)
# Stop. No need for a sleep here because we're done.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
print("Stop. No need for a sleep here because we're done")