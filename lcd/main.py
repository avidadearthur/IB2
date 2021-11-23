#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime
from subprocess import *
import lcddriver
import threading

global HASINPUT
HASINPUT = False

global SENTENCE
SENTENCE = ''


def worker():
    # Do some stuff
    print("t thread started successfully ")
    print([th.name for th in threading.enumerate()])
    lcd.lcd_display_string(SENTENCE, 1)
    print("Closing t thread... ")
    sleep(3)


def get_sentence():
    print("s thread started successfully ")
    print([th.name for th in threading.enumerate()])
    SENTENCE = input("Enter a sentence: ")
    print(SENTENCE)
    HASINPUT = True
    print("Closing s thread... ")
    sleep(1)


def run_cmd(cmd):
    p = Popen(cmd, shell = True, stdout = PIPE)
    output = p.communicate()[0]
    return output


if __name__ == "__main__":
    # if you call this script from the command line (the shell) it will
    # run the 'main' function

    lcd = lcddriver.lcd()

    while True:

        # date & time display
        lcd.lcd_clear()

        lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
        lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)

        sleep(1)

        print([th.name for th in threading.enumerate()])

        if not HASINPUT:
            s = threading.Thread(target=get_sentence, name="s")
            s.start()

        # thread checking
        if "t" not in [th.name for th in threading.enumerate()] and HASINPUT:

            HASINPUT = False
            SENTENCE = ''
            s.join()
            print([th.name for th in threading.enumerate()])

            print("Starting t thread...")
            lcd.lcd_clear()
            t = threading.Thread(target=worker, name="t")  # Always put a comma after the arguments. Even if you have only one arg.
            t.start()  # Start the thread
            t.join()  # Join main thread to avoid competition over display

        if SENTENCE == "stop":
            print("Waiting for the function to finish...")
            t.join()  # Stop the thread (NOTE: the program will wait for the function to finish)
            break
        else:
            print("Thread closed")


