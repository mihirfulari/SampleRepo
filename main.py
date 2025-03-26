from machine import Pin, SPI
import pcd8544_fb
from ota import OTAUpdater
from time import sleep

# Initialize SPI (HSPI) interface
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)

# Define control pins
cs = Pin(2, Pin.OUT)   # Chip Select (CE)
dc = Pin(15, Pin.OUT)  # Data/Command (DC)
rst = Pin(0, Pin.OUT)  # Reset (RST)
bl = Pin(12, Pin.OUT)  # Backlight (BL), optional

# Initialize the LCD
lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

# Clear the display
lcd.fill(0)

# Display text
lcd.text("-----------", 0, 0)
lcd.text("<3",0,10)
lcd.text("-----------", 0, 40)
lcd.show()
