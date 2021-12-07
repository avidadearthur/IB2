from gpiozero import MCP3008
from time import sleep
import math

ldr = MCP3008(channel=0)

while True:
    
    value = ldr.value
    print(value)

    voltage = value / 255.0 * 3.3
    Rt = 10 * voltage / (3.3 - voltage)
    tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0) 
    tempC = tempK -273.15
    print ('ADC Value : %d, Voltage : %.2f, Temperature : %.2f'%(value,voltage,tempC))
    sleep(0.01)

    sleep(0.5)