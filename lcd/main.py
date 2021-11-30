#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime
import lcddriver
import threading
import keyboard

def display_sentence(input_sentence):
    # Do some stuff
    print("Thread started successfully ")
    lcd.lcd_display_string(input_sentence, 1)
    print("Closing thread... ")
    sleep(3)


def clock():
    while True:
        # date & time display
        if "sentence" not in [th.name for th in threading.enumerate()]:
            lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
            lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)
            sleep(1)
        if off:
            break


if __name__ == "__main__":
    # if you call this script from the command line (the shell) it will
    # run the 'main' function
    lcd = lcddriver.lcd()

    global off
    off = False
    clock_thread = threading.Thread(target=clock, name="clock")
    clock_thread.start()

    while True:

        print([th.name for th in threading.enumerate()])

        if keyboard.is_pressed('a'):

            # thread checking
            if "sentence" not in [th.name for th in threading.enumerate()]:
                sentence = "'A' Key was pressed"
                print("Starting thread...")

                lcd.lcd_clear()
                # Always put a comma after the arguments.
                # Even if you have only one arg.
                sentence_display = threading.Thread(target=display_sentence, args=(sentence,), name="sentence")
                sentence_display.start()  # Start the thread
                sentence_display.join()  # Join main thread to avoid competition over display

        if keyboard.is_pressed('b'):
            print("Waiting for the function to finish...")
            sentence_display.join()  # Stop the thread (NOTE: the program will wait for the function to finish)
            # Break the clock thread
            off = True
            break
        else:
            print(sentence)
            print("Thread closed")
