# Import modules
import RPi.GPIO as GPIO 
from time import sleep, strftime, time
import lcddriver
import threading


def alarm():

    sleep(1)
    # Always start by clearing the LCD
    lcd.lcd_clear()

    while True:

        lcd.lcd_display_string('Set your alarm: ', 1)
        lcd.lcd_display_string('%d:%d:00'.format(), 2)
        # Stop displaying during SET
        
        if GPIO.input(11) == GPIO.HIGH:
            break



def clock():

    sleep(1)
    # Always start by clearing the LCD
    lcd.lcd_clear()

    while True:
        
        # Date & Time display
        lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
        lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)

        # Stop displaying during SET
        if GPIO.input(11) == GPIO.HIGH:
            break


if __name__ == "__main__":

    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    # Set pins to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # SET   GPIO23
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # UP    GPIO22
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # DOWN  GPIO27
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # RESET GPIO17

    lcd = lcddriver.lcd()

    print("Starting clock thread...")
    sleep(1)
    clock_thread = threading.Thread(target=clock, name="clock")
    clock_thread.start()

    while True:
        
        if GPIO.input(16) == GPIO.HIGH:
            
            # check if there's already an alarm set
            if "alarm" not in [th.name for th in threading.enumerate()]:
                print("Starting thread...")
                sleep(1)

                alarm_thread = threading.Thread(target=alarm, name="alarm")
                alarm_thread.start()  # Start the thread
                #alarm_thread.join()  # Join main thread to avoid competition over display