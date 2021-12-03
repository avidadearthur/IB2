from gpiozero import MCP3008
from time import sleep

ldr = MCP3008(channel=0)

while True:
    print(ldr.value)
    sleep(0.5)