from time import sleep
import math

ldr = MCP3008(channel=1)

while True:

    value = ldr.value
    print(value)
    sleep(1)