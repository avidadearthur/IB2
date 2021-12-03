from gpiozero import MCP3008
from time import sleep

ldr = MCP3008(channel=0, 
    clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=5)

while True:
    print(ldr.value)
    sleep(0.5)