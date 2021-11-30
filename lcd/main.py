#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime, time
import lcddriver
import threading
import RPi.GPIO as GPIO

def display_sentence(input_sentence):
    # Do some stuff
    print("Thread started successfully ")
    lcd.lcd_display_string(input_sentence, 1)
    print("Closing thread... ")
    sleep(3)


def clock():
    # to be used during testing
    t_end = time() + 30 # add timer for clock loop

    while True:
        # date & time display
        if "sentence" not in [th.name for th in threading.enumerate()]:
            lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
            lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)
            sleep(1)
        if off:
            break
        # avoid infinite loop due to errors
        if time() > t_end:
            break


if __name__ == "__main__":
    # if you call this script from the command line (the shell) it will
    # run the 'main' function

    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 8 to be an input pin and set initial value to be pulled low (off)

    lcd = lcddriver.lcd()

    global off
    off = False
    clock_thread = threading.Thread(target=clock, name="clock")
    clock_thread.start()

    while True:

        #print([th.name for th in threading.enumerate()])

        # It might be a good idea to block the GPIO once it is pressed
        # to avoid bugs
        if GPIO.input(10) == GPIO.HIGH:

            # thread checking
            if "sentence" not in [th.name for th in threading.enumerate()]:
                sentence = "GPIO 10 was set to high"
                print("Starting thread...")

                lcd.lcd_clear()
                # Always put a comma after the arguments.
                # Even if you have only one arg.
                sentence_display = threading.Thread(target=display_sentence, args=(sentence,), name="sentence")
                sentence_display.start()  # Start the thread
                sentence_display.join()  # Join main thread to avoid competition over display

        if GPIO.input(8) == GPIO.HIGH:
            print("Waiting for the function to finish...")
            #sentence_display.join()  # Stop the thread (NOTE: the program will wait for the function to finish)
            # Break the clock thread
            off = True
            break
