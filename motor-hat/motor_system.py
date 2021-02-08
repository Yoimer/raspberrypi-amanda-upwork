# please install the libraries from here
# https://github.com/adafruit/Adafruit_CircuitPython_DHT

# adafruit libraries
import board
import adafruit_dht

import time

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

#motor hat section 
from adafruit_motorkit import MotorKit
kit = MotorKit(0x40)

while True:
    try:

        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

        # motor direction based on temperature
        if((temperature_c >= 24.0) and (temperature_c <= 29.0)):
            # moves forward
            kit.motor1.throttle = 1.0
            kit.motor2.throttle = 1.0
            print("Forward")
            time.sleep(2.0)
            kit.motor1.throttle = 0.0
            kit.motor2.throttle = 0.0
        elif(temperature_c >= 30.0):
            # moves backward
            kit.motor1.throttle = -0.75
            kit.motor2.throttle = -0.75
            print("Backward")
            time.sleep(2.0)
            kit.motor1.throttle = 0.0
            kit.motor2.throttle = 0.0

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(4.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(4.0)