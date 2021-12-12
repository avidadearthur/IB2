#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime, time

from gpiozero import exc
import lcddriver
import threading
import RPi.GPIO as GPIO


if __name__ == "__main__":
    
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    # Set pins to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # SET   GPIO23
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # UP    GPIO22
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # DOWN  GPIO27
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # RESET GPIO17

    lcd = lcddriver.lcd()

    # Possible states: 
    # 0 - Clock Date & Time
    # 1 - Sensors Data
    # 2 - Alarm Set/Alarm Display

    try:
        curr_state = 0 # Set 0 as default state
        while True:
            # Use UP and DOWN GPIOs to move between states
            # Arrow UP
            if GPIO.input(15) == GPIO.HIGH:
                if curr_state <= 2:
                    curr_state = curr_state + 1
                else:
                    curr_state = 0

            # Arrow DOWN
            if GPIO.input(13) == GPIO.HIGH:
                if curr_state >= 0:
                    curr_state = curr_state - 1
                else:
                    curr_state = 2

            # 0 - Clock Date & Time
            if abs(curr_state) == 0:
                sleep(1)
                lcd.lcd_clear()
                lcd.lcd_display_string('Clock date & time', 1)
            
            # 1 - Sensors Data
            elif abs(curr_state) == 1:
                sleep(1)
                lcd.lcd_clear()
                lcd.lcd_display_string('Sensors Data', 1)
            
            # 2 - Alarm Set/Alarm Display
            elif abs(curr_state) == 2:
                sleep(1)
                lcd.lcd_clear()
                lcd.lcd_display_string('Alarm', 1)

    except KeyboardInterrupt:
        lcd.lcd_clear()

    
    
