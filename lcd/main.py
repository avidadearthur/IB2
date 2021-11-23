#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime
from subprocess import *
import lcddriver
import threading


def worker(num):
    # Do some stuff
    for i in range(5):
        sleep(2)
        print(2**(num + i))

def run_cmd(cmd):
    p = Popen(cmd, shell = True, stdout = PIPE)
    output = p.communicate()[0]
    return output


if __name__ == "__main__":
    # if you call this script from the command line (the shell) it will
    # run the 'main' function

    lcd = lcddriver.lcd()

    lcd.lcd_clear()

    i = int(input("Enter a number: "))

    t = threading.Thread(target=worker, args=(i,))  # Always put a comma after the arguments. Even if you have only one arg.
    t.start() # Start the thread

    while True:

        choice = input("Waiting for input: ")

        if choice == "stop":
            print("Waiting for the function to finish...")
            t.join()  # Stop the thread (NOTE: the program will wait for the function to finish)
            break

        else:
            print(choice)

        lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
        lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)

        sleep(1)

