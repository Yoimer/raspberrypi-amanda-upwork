# # pins configuration

# #VCC GPS ----> 1RPI (3.3V)
# #GND GPS ----> 6RPI (GND)
# #TX GPS  ----> GPIO15 RPI (RXD)
# #RX GPS  ----> GPIO14 RPI (TXD)

import serial,time,pynmea2

port = '/dev/serial0'
baud = 9600

serialPort = serial.Serial(port, baudrate = baud, timeout = 0.5)
while True:
    str = serialPort.readline().decode().strip()
    print(str)
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print("  Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.latitude,msg.lat_dir,msg.longitude,msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats))
    time.sleep(0.1)