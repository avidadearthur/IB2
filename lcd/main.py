#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime
from subprocess import *
import lcddriver
import threading


def worker(sentence):
    # Do some stuff
    print("Thread started successfully ")
    lcd.lcd_display_string(sentence, 1)
    sleep(3)


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

        sentence = input("Enter a sentence: ")

        # thread checking
        if "t" not in [th.name for th in threading.enumerate()]:
            print("Starting thread...")
            lcd.lcd_clear()
            t = threading.Thread(target=worker, args=(sentence,), name="t")  # Always put a comma after the arguments. Even if you have only one arg.
            t.start()  # Start the thread

        elif sentence == "stop":
                print("Waiting for the function to finish...")
                t.join()  # Stop the thread (NOTE: the program will wait for the function to finish)
                break

        else:
            print(sentence)


