import threading
import RPi.GPIO as GPIO
from time import strftime
import lcddriver

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # RESET GPIO17


def display_clock(lcd, clock_thread=None):
    # Always start by clearing the LCD
    lcd.lcd_clear()

    while True:

        if "alarm" not in [th.name for th in threading.enumerate()]:
            if "sensors" not in [th.name for th in threading.enumerate()]:
                # Date & Time display
                lcd.lcd_display_string(strftime('TIME: ' '%H:%M:%S'), 1)
                lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)

        # Stop displaying
        if GPIO.input(15) == GPIO.HIGH or GPIO.input(13) == GPIO.HIGH:
            try:
                clock_thread.join()
            except RuntimeError:
                break

            break

        # RESET button
        if GPIO.input(11) == GPIO.HIGH:
            break
