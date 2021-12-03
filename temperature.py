from gpiozero import MCP3008
from time import sleep

ldr = MCP3008(channel=0, 
    clock_pin=23, mosi_pin=19, miso_pin=21, select_pin=29)

while True:
    print(ldr.value)
    sleep(0.5)