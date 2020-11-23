# please install the libraries from here
# https://github.com/adafruit/Adafruit_CircuitPython_DHT

# adafruit libraries
import board
import adafruit_dht

# time libraries
import time
from datetime import datetime

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
headers = "Date,Time,Temperature,Humidity" + "\r\n"
csv_file_name = "/home/pi/Desktop/dht22/datalogger.csv"

# function tthat writes readings to csv
def write_content_to_csv():
    print("writing content to csv!!!")
    f = open(csv_file_name, "a+")
    for i in range(0, len(list_to_file)):
        print(list_to_file[i])
        # saves each reading on csv
        f.write(list_to_file[i])

    # adds new line for next reading
    f.write("\r\n")
    # cleans lists for next reading
    list_to_file.clear()
    f.close()

while True:
    try:
        # list of values to be saved on csv
        list_to_file = []

        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")

        list_to_file.append(str(date) + ",")
        list_to_file.append(str(current_time) + ",")
        list_to_file.append(str(temperature_c) + ",")
        list_to_file.append(str(humidity))
        
        # checks if file already exists
        if(os.path.isfile(csv_file_name)):
            print("File exists")
            write_content_to_csv()
        else:
            print("File does not exist")
            # creates file including headers
            f = open(csv_file_name, "a+")
            f.write(headers)
            f.close()
            write_content_to_csv()

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)