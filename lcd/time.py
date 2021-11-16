#!/usr/bin/env python3.2.3
#Date And Time Script

from time import sleep, strftime
from subprocess import *
import lcddriver

lcd = lcddriver.lcd()


def run_cmd(cmd):
    p = Popen(cmd, shell = True, stdout = PIPE)
    output = p.communicate()[0]
    return output

lcd.lcd_clear()

while True:
    lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
    lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)

    sleep(1)