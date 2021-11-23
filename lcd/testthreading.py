from time import sleep, strftime
from subprocess import *
import lcddriver
import threading

lcd = lcddriver.lcd()

def worker(num):
    # Do some stuff
    for i in range(5):
        time.sleep(2)
        print(2**(num + i))

if __name__ == "__main__":
    i = int(input("Enter a number: "))

    t = threading.Thread(target=worker, args=(i,)) # Always put a comma after the arguments. Even if you have only one arg.
    t.start() # Start the thread

    while True:
        choice = input("Wating for input: ")

        if choice == "stop":
            print("Waiting for the function to finish...")
            t.join() # Stop the thread (NOTE: the program will wait for the function to finish)
            break

        else:
            print(choice)

        #clock stuff
        lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
        lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)

        sleep(1)