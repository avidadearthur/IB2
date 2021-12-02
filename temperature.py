import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import spidev
import math
from time import sleep

## PINOUT BCM ##
CLK = 23
MISO = 21
MOSI = 19
CS = 24


tempChannel = 0
sleepTime = 1

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS,miso=MISO,mosi=MOSI) 
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(1,0))
def mcpRead(channel):
    return mcp.read_adc(channel)


while (1):
    adc = mcpRead(tempChannel)
    print(adc)
    inBeta = 1.0/3950.0
    inTO = 1.0/298.15
    k = 1.0/(inTO+inBeta*math.log(1023/adc-1.0))
    temperature = k-273.15
    print("Temp: %s"%(temperature))
    sleep(sleepTime)