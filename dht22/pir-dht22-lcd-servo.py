# please install the libraries from here
# https://github.com/adafruit/Adafruit_CircuitPython_DHT

# adafruit libraries
import board
import adafruit_dht

import RPi.GPIO as GPIO
# setup the GPIO pin for the servo
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# setup PWM process
pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)
# Start PWM running, with value of 0 (pulse off)
pwm.start(0)

# setup for pir
GPIO.setup(23, GPIO.IN)                 #Read output from PIR motion sensor
GPIO.setup(2, GPIO.OUT)                 #LED output pin
GPIO.setup(27, GPIO.OUT)                #Set buzzer - pin 27 (27) as output

# time libraries
import time
from datetime import datetime

# path libraries
import os.path

# pwm = pulseio.PWMOut(board.D17, frequency=50)
# servo = servo.Servo(pwm, min_pulse=0, max_pulse=2000)

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

# display libraries
# lcddriver.py and i2c_lib.py have to be on the root folder (in our case is dht22)
import lcddriver
import time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

# function tthat writes readings to csv
def write_content_to_csv():
    print("writing content to csv!!!")
    f = open(path + folder_name + csv_file_name, "a+")
    for i in range(0, len(list_to_file)):
        print(list_to_file[i])
        # saves each reading on csv
        f.write(list_to_file[i])

    # adds new line for next reading
    f.write("\r\n")
    # cleans lists for next reading
    list_to_file.clear()
    f.close()

def rotate_servo_to_zero_degrees():
    print("rotate_servo_to_zero_degrees!!")
    long_string(display, "Servo is 0 dgrs", 1)
    pwm.ChangeDutyCycle(2+(0.0/18))
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

def rotate_servo_to_180_degress():
    print("rotate_servo_to_180_degress!!")
    long_string(display, "Servo is 180 dgrs", 1)
    pwm.ChangeDutyCycle(2+(180.0/18))
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

def long_string(display, text = '', num_line = 1, num_cols = 20):
    """ 
    Parameters: (driver, string to print, number of line to print, number of columns of your display)
    Return: This function send to display your scrolling string.
    """
    if(len(text) > num_cols):
        display.lcd_display_string(text[:num_cols],num_line)
        time.sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print,num_line)
            time.sleep(0.2)
            time.sleep(1)
    else:
        display.lcd_display_string(text,num_line)

# functions that activates and deactivates buzzer
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
    try:

        # pir section
        i = GPIO.input(23)
        if i == 0:                             #When output from motion sensor is LOW
            print("No intruders",i)
            GPIO.output(2, GPIO.LOW)          #Turn OFF LED
            time.sleep(0.1)                      # Delay in seconds
            #no beeping
            GPIO.output(27, GPIO.LOW)
        elif i == 1:                           #When output from motion sensor is HIGH
            while (GPIO.input(23) == 1):
                print("Intruder detected",i)
                GPIO.output(2, GPIO.HIGH)      #Turn ON LED
                time.sleep(0.1)
                triggerbuffer();

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

        # servo angle based on temperature
        if((temperature_c >= 24.0) and (temperature_c <= 29.0)):
            rotate_servo_to_zero_degrees()
            degrees = 0
        elif(temperature_c >= 30.0):
            rotate_servo_to_180_degress()
            degrees = 180

        # display readings on LCD
        print("Writing to display")
        long_string(display, "Temp: " + str(temperature_c) + "C", 2)
        time.sleep(1.5)
        long_string(display, "Humd: "+ str(humidity) + "%", 2)
        time.sleep(1)

        # display.lcd_display_string("Temp: " + str(temperature_c) + "C", 1) # Write line of text to first line of display
        # display.lcd_display_string("Humd: "+ str(humidity) + "%", 2) # Write line of text to second line of display

        # folder creation
        # each month a folder will be create with the format December-2020, January-2021 etc..
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        current_month = now.strftime('%B')
        current_year = now.strftime("%Y")
        current_time = now.strftime("%H:%M:%S")
        folder_name = current_month + '-' + current_year + '/'

        # checks if folder already exists
        path = "/home/pi/Desktop/dht22/"
        if not os.path.exists(path + folder_name):
            print("Folder does not exist, creating...")
            os.makedirs(path + folder_name)
        else:
            print("Folder exists")

        # csv creation
        headers = "Date,Time,Temperature,Humidity,Servo Rotation (Degrees)" + "\r\n"
        # each file will have as format 01-12-2020.csv and so on
        csv_file_name = now.strftime("%d-%m-%Y") + ".csv"

        list_to_file.append(str(date) + ",")
        list_to_file.append(str(current_time) + ",")
        list_to_file.append(str(temperature_c) + ",")
        list_to_file.append(str(humidity) + ",")
        list_to_file.append(str(degrees))

        # checks if file already exists
        if(os.path.isfile(path + folder_name + csv_file_name)):
            print("File exists")
            write_content_to_csv()
        else:
            print("File does not exist, creating...")
            # creates file including headers
            f = open(path + folder_name + csv_file_name, "a+")
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