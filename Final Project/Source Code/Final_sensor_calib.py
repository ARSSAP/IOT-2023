import busio 
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import board
import time
import math
import RPi.GPIO as GPIO
import Adafruit_DHT

#Variables
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 7
RESIST_SENSOR = 1024
RESIST_LOAD = 1024
SENSOR_VOLT = 5.0
CONST_A = 116.6020682
CONST_B = 2.769034857
#Functions


    



def AirQualityCalculation(AQ_VOL):
    RESISTANCE = RESIST_SENSOR * (SENSOR_VOLT - AQ_VOL) / AQ_VOL
    PREASURE_PER_MINUTE = CONST_A * math.pow(RESISTANCE / RESIST_LOAD,CONST_B)
    return PREASURE_PER_MINUTE

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

run = True
while run:

    # Calculating Air Quality
    AQ_VOL = channel0.voltage
    RESISTANCE = RESIST_SENSOR * (SENSOR_VOLT - AQ_VOL) / AQ_VOL
    AQ_CAL = CONST_A * math.pow(RESISTANCE / RESIST_LOAD,CONST_B)
    AQ_VAL = round(AQ_CAL,2)
    print(str(AQ_VAL)+" : Air Quality")
    time.sleep(1)

    # Calculating Light Detection
    LDR_VOL = 5 * channel1.value /(RESIST_SENSOR +channel1.value ) 
    LDR_VAL = round(LDR_VOL,2)
    print(str(LDR_VAL)+" : Light Detection")
    time.sleep(1)

    # Calculating Tempreature
    TEM_VOL = channel2.voltage
    TEM_VAL = round(((TEM_VOL)-500)/18.333,6) 
    TEM_CEL = -TEM_VAL 
    TEM_FAR = ((TEM_CEL*1.8)+32)
    print(str(TEM_CEL)+" : Tempreature in celcius")
    print(str(TEM_FAR)+" : Tempreature in Farhenheit")
    time.sleep(1)

    # Calculating Humidity
    HUM_VOL = channel3.value
    HUM_VAL = round(HUM_VOL + channel3.voltage,2)
    print(str(HUM_VOL)+" : Humidity")
    time.sleep(5)
