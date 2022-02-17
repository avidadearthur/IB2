import spidev
import time
import os
 
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
 
  R_o = 9680 
  voltz_src = 3.3
 
  R_t = R_o * (( voltz_src / voltz_out ) - 1)
 
  temp = R_t
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