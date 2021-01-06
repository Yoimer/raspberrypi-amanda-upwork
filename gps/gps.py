# # pins configuration

# #VCC GPS ----> 1RPI (3.3V)
# #GND GPS ----> 6RPI (GND)
# #TX GPS  ----> GPIO15 RPI (RXD)
# #RX GPS  ----> GPIO14 RPI (TXD)

import serial,time,pynmea2
import requests
import json

port = '/dev/serial0'
baud = 9600

serialPort = serial.Serial(port, baudrate = baud, timeout = 0.5)
while True:
    gpsdata = serialPort.readline().decode().strip()
    print(gpsdata)
    if gpsdata.find('GGA') > 0:
        msg = pynmea2.parse(gpsdata)
        print("  Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.latitude,msg.lat_dir,msg.longitude,msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats))
        # if gps gets latitude and longitude, do the reverse geolocation using locationiq api
        if ( (msg.latitude != 0.0) and (msg.longitude != 0.0) ):
            current_location = requests.get('https://us1.locationiq.com/v1/reverse.php?key=pk.8ee983dc1c3bd684d339c83b46d1c897&lat=' + str(msg.latitude) + '&' + 'lon=' + str(msg.longitude) + '&format=json')
            current_location = dict(json.loads(current_location.text))
            print("Your current location is: {}".format(current_location["display_name"]))
            time.sleep(2)
    time.sleep(0.1)