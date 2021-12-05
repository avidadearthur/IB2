import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep, strftime, time
import lcddriver


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pins to be an input pin and set initial value to be pulled low (off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # SET   GPIO23
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # UP    GPIO22
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # DOWN  GPIO27
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # RESET GPIO17

lcd = lcddriver.lcd()

while True:
    lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
    lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)
    sleep(1)