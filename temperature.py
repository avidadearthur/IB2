## PINOUT BCM ##
#CLK = 23
#MISO = 21
#MOSI = 19
#CS = 24

from gpiozero import MCP3008
from time import sleep

ldr = MCP3008(channel=0, 
    clock_pin=23, mosi_pin=19, miso_pin=21, select_pin=24)

while True:
    print(ldr.value)
    sleep(0.5)