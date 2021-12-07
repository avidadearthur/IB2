from gpiozero import MCP3008
from time import sleep
import math

ldr = MCP3008(channel=0)

while True:

    value = ldr.value
    print(value)

    voltage = value * 3.3
    Rt = value * 9.6
    tempK = 1 / (1/(273.15 + 25) + math.log(Rt/9.6)/2000)
    
    tempC = tempK -273.15
    print ('NTC resistance : %.2f k, Voltage : %.2f, Temperature : %.2f'%(Rt,voltage,tempC))

    sleep(1)