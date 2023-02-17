#Importing Libraries
import sys
import busio 
import adafruit_ads1x15.ads1115 as ADS
from datetime import date, datetime
from adafruit_ads1x15.analog_in import AnalogIn
import board
import time
import math
import RPi.GPIO as GPIO
import Adafruit_DHT
import numpy as np
from pymongo import MongoClient
import Lcd_driver as lcd
import pymongo
import urllib 


#variables
done = False #Loader status
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 7
RESIST_SENSOR = 1024
RESIST_LOAD = 1024
SENSOR_VOLT = 5.0
CONST_A = 116.6020682
CONST_B = 2.769034857
MONGODB_USER="ars"
MONGODB_PASS="348261"
MONGODB_DB = 'weather_monitoring_db'
MONGODB_COLLECTION = 'sensor_data'


#for weather comparisions
sunny = {'air_quality': 50, 'light _detection': 5.0, 'temperature': 48, 'humidity': 2500}
clear = {'air_quality': 100, 'light _detection': 4.5, 'temperature': 33, 'humidity': 2000}
windy = {'air_quality': 150, 'light _detection': 2.5, 'temperature': 27, 'humidity': 3000}
Humid = {'air_quality': 10, 'light _detection': 1.5, 'temperature': 45, 'humidity': 4000}
warm = {'air_quality': 50, 'light _detection': 1.0, 'temperature': 50, 'humidity': 4000}
cold = {'air_quality': 20, 'light _detection': 2.5, 'temperature': 10, 'humidity': 1000}
hot = {'air_quality': 40, 'light _detection': 5.5, 'temperature': 58, 'humidity': 50000}

#Calling SCL & SDA ports from Pi Board
i2c = busio.I2C(board.SCL, board.SDA)  
ads = ADS.ADS1115(i2c)
ads.gain = 1

#instance for spidev for sensor value conversion
 

#Assigning Channel of ADS1115 to sensors
channel0 = AnalogIn(ads, ADS.P0) # For LDR sensor
channel1 = AnalogIn(ads, ADS.P1) # For Turbidity sensor
channel2 = AnalogIn(ads, ADS.P2) # For TDS sensor
channel3 = AnalogIn(ads, ADS.P3) # For WaterFlow sensor

# Connection string for MongoDB
def mongo_db_connection():
    CONNECTION_STRING = "mongodb+srv://pi4:"+MONGODB_PASS+"@cluster0.wbrzjmu.mongodb.net/test"
    
    try:
        client = MongoClient(CONNECTION_STRING)
        dbname = client[MONGODB_DB]
        collection_name = dbname[MONGODB_COLLECTION]
        print("Database connected successfully!")
        return collection_name 
    except:
        print("Database could not be connected!")

#Startup Function
def StartMainFunc():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("       WEATHER MONITORING SYSTEM       ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#Lcd Driver Function
def displayLCD(LINE_,VALUE,ALIGN):
    LINE_NUMBER = {1: lcd.LCD_LINE_1,2: lcd.LCD_LINE_2}
    lcd.lcd_init()
    lcd.lcd_byte(LINE_NUMBER[LINE_], lcd.LCD_CMD)
    lcd.lcd_string(str(VALUE),ALIGN)

#loader Function
def loader():
    while done == False:
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


def SensorCaliberation(value,iterations):
    sample_list = []
    for i in range(iterations):
        sample_list.append(value)
    time.sleep(2)
    return np.mean(sample_list)
    

def LcdDisplay():
    pass

def MonitorWeather(air_qlty,tempreature,humidity,ldr):

    pass

run = True
while run:

    # Calculating Air Quality
    AQ_VOL = SensorCaliberation(channel0.voltage,5)
    RESISTANCE = RESIST_SENSOR * (SENSOR_VOLT - AQ_VOL) / AQ_VOL
    AQ_CAL = CONST_A * math.pow(RESISTANCE / RESIST_LOAD,CONST_B)
    AQ_VAL = round(AQ_CAL,2)
    print(str(AQ_VAL)+" : Air Quality")
    time.sleep(1)

    # Calculating Light Detection
    LDR_VOL = 5 * SensorCaliberation(channel1.voltage,5) /(RESIST_SENSOR +channel1.value ) 
    LDR_VAL = round(LDR_VOL,2)
    print(str(LDR_VAL)+" : Light Detection")
    time.sleep(1)

    # Calculating Tempreature
    TEM_VOL = SensorCaliberation(channel2.voltage,5)
    TEM_VAL = round(((TEM_VOL)-500)/18.333,6) 
    TEM_CEL = -TEM_VAL 
    TEM_FAR = ((TEM_CEL*1.8)+32)
    print(str(TEM_CEL)+" : Tempreature in celcius")
    print(str(TEM_FAR)+" : Tempreature in Farhenheit")
    time.sleep(1)

    # Calculating Humidity
    HUM_VOL = SensorCaliberation(channel3.voltage,5)
    HUM_VAL = round(HUM_VOL + channel3.voltage,2)
    print(str(HUM_VAL)+" : Humidity")
    time.sleep(5)
    
    #Display Variable Setup
    LINE1="AQ:" + str(round(AQ_VAL,2)) + ", LDR:" + str(round(LDR_VAL,2))
    LINE2="TEMP:" + str(round(TEM_CEL,2)) + ", HUM:" + str(round(HUM_VAL,2))

    AQ_CHECK = AQ_VAL >= PH_STANDARD_RANGE[0] and PH_VAL <= PH_STANDARD_RANGE[1]
    LDR_CHECK = LDR_VAL >= TUR_STANDARD_RANGE[0] and TUR_VAL <= TUR_STANDARD_RANGE[1]
    TEM_CEL_CHECK = TEM_CEL >= TDS_STANDARD_RANGE[0] and TDS_VAL <= TDS_STANDARD_RANGE[1]
    HUM_CHECK = HUM_VAL >= WF_STANDARD_RANGE[0] and WF_VAL <= WF_STANDARD_RANGE[1]

    # IS_DRINKABLE = (IS_PH_OK and IS_TUR_OK and IS_TDS_OK)
    # STATUS = "CLEAN" if IS_DRINKABLE else "POLLUTED"

    #Database schema 
    sensor_data = {
            "airqlty_sensor_value" : str(AQ_VAL),
            "lightdetection_sensor_value" : str(LDR_VAL),
            "temperatureincel_sensor_value" : str(TEM_CEL),
            "temeperatureinfar_sensor_value" : str(TEM_FAR),
            "humidity_sensor_value" : str(HUM_VAL),
            "status" : "ok",
            "date_added":   datetime.now()
            }

    #Establisting Database Connection     
    db =  mongo_db_connection()
    time.sleep(5)

    print("Weather is ", STATUS)
    displayLCD(1,"Weather: " + STATUS,1)
    try:
        db.insert_one(sensor_data)
        print("Data logged successfully in db")
    except:
        print("Data not inserted in db")

    # Display on Lcd                                                                                                                                            
    displayLCD(1,LINE1,1)
    displayLCD(2,LINE2,2)
    

    #Stroing local logs
    logs = str(datetime.now()),": Air Quality: ",str(AQ_VAL),", Light Detection: ",str(LDR_VAL),", Temperature in Celcius: ",str(TEM_CEL),", Temperature in Farhenheit: ",str(TEM_FAR),", Humidity: ",str(HUM_VAL) + "\n"
    print(logs)
    file = open("logs.txt","a")
    file.writelines(logs)
    file.close()
