from gpiozero import MCP3008
from time import sleep
import math

ldr = MCP3008(channel=0)

while True:

    
    # Resitor - 9.6k
    # NTC     - 3.36k @25C
    #
    # T2 = 1/(1/T1 + ln(Rt/R)/B)
    #
    # Rt - is the thermistor’s resistance under T2 temperature
    #
    # R  - is the nominal resistance under T1 temperature - 9.6k 
    #
    # B is the thermal index - 2880k
    #
    # T1, T2 is the temperature in Kelvin
    # We’ll use 25 for T1
    
    value = ldr.value
    print(value)

    voltage = value * 3.3
    Rt = value * 3.36
    tempK = 1 / (1/(273.15 + 25) + math.log(Rt/9.6)/2880)
    
    tempC = tempK -273.15
    print ('NTC resistance : %d k, Voltage : %.2f, Temperature : %.2f'%(Rt,voltage,tempC))
