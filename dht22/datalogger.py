# please install the libraries from here
# https://github.com/adafruit/Adafruit_CircuitPython_DHT

# adafruit libraries
import time
import board
import adafruit_dht


# path libraries
import os.path

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

# Date/Time/ Temperature/Humidity



# csv creation
headers = "Date,Time,Temperature °C,Humidity %" + "\r\n"
csv_file_name = "/home/pi/dht22/datalogger.csv"

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

        # checks if file already exists
        if(os.path.isfile(csv_file_name)):
            print("File exists")
        else:
            print("File does not exist")
            # creates file including headers
            f = open(csv_file_name, "a+")
            f.write(headers)
            f.close()

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
