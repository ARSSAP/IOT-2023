import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import lcd



def displayLCD(LINE_,VALUE,ALIGN):
    LINE_NUMBER = {1: lcd.LCD_LINE_2,2: lcd.LCD_LINE_1}
    lcd.lcd_init()
    lcd.lcd_byte(LINE_NUMBER[LINE_], lcd.LCD_CMD)
    lcd.lcd_string(str(VALUE),ALIGN)

while True:
   IS_DRINKABLE = True
   STATUS = "Polluted"
   LINE1 = "line1"
   LINE2= "line2"
   if IS_DRINKABLE:
    print("Water is ", STATUS)
    displayLCD(1,"Water: " + STATUS,1)
    time.sleep(5)
    displayLCD(1,LINE1,1)
    displayLCD(2,LINE2,2)