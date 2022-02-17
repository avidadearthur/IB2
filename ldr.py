import spidev
import time
import os
from numpy import log as ln
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
# Function to calculate temperature from
# NTC data, rounded to specified
# number of decimal places.
def ConvertTemp(voltz_out,places):
 
  R_o = 9660 
  voltz_src = 3.3

  R_ref = 5000
  A = 3.35402e-03
  B = 2.51094e-04
  C = 3.51094e-04
  D = 1.10518e-07
 
  R_t = (R_o * voltz_out)/(voltz_src-voltz_out)

  temp = (A + B*ln(R_t/R_ref) + C*(ln(R_t/R_ref)**2) + D*(ln(R_t/R_ref)**3))**(-1)
  temp = round(temp,places)
  
  return temp
 
# Define sensor channels
light_channel = 1
temp_channel  = 0
 
# Define delay between readings
delay = 5
 
while True:
 
  # Read the light sensor data
  light_level = ReadChannel(light_channel)
  light_volts = ConvertVolts(light_level,2)
 
  # Read the temperature sensor data
  temp_level = ReadChannel(temp_channel)
  temp_volts = ConvertVolts(temp_level,2)
  temp       = ConvertTemp(temp_volts,2)
 
  # Print out results
  print "--------------------------------------------"
  print("Light: {} ({}V)".format(light_level,light_volts))
  print("Temp : {} ({}V) {} Ohms".format(temp_level,temp_volts,temp))
 
  # Wait before repeating loop
  time.sleep(delay)