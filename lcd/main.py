#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime, time

import lcddriver
import sensors
import ldr
import threading
import RPi.GPIO as GPIO

def alarm():
    
    sleep(1)
    lcd.lcd_clear()
    
    
    while True:

        if "clock" not in [th.name for th in threading.enumerate()]:
            if "sensors" not in [th.name for th in threading.enumerate()]:
                lcd.lcd_display_string('Alarm', 1)

        # Stop displaying
        if GPIO.input(15) == GPIO.HIGH or GPIO.input(13) == GPIO.HIGH:
            try:
                alarm_thread.join()
            except RuntimeError:
                break

            break
            
        # RESET button
        if GPIO.input(11) == GPIO.HIGH:
            break

def display_sensors():
    
    sleep(1)
    lcd.lcd_clear()
    
    while True:

        if "clock" not in [th.name for th in threading.enumerate()]:
            if "alarm" not in [th.name for th in threading.enumerate()]:
                lcd.lcd_display_string('Sensors Data', 1)
                # Code for the sensors
                # Define sensor channels
                light_channel = 1
                temp_channel  = 0

                # Define delay between readings

                # Read the light sensor data
                light_level = sensors.ReadChannel(light_channel)
                light_volts = sensors.ConvertVolts(light_level,2)
 
                # Read the temperature sensor data
                temp_level = sensors.ReadChannel(temp_channel)
                temp_volts = sensors.ConvertVolts(temp_level,2)
                temp       = sensors.ConvertTemp(temp_volts,2)
 
                # Print out results to lcd screen
                lcd.lcd_display_string("Temp : {} C".format(temp),2)

            
        # Stop displaying
        if GPIO.input(15) == GPIO.HIGH or GPIO.input(13) == GPIO.HIGH:
            try:
                sensors_thread.join()
            except RuntimeError:
                break

            break
            
        # RESET button
        if GPIO.input(11) == GPIO.HIGH:
            break
    

def clock():

    sleep(1)
    # Always start by clearing the LCD
    lcd.lcd_clear()

    while True:

        if "alarm" not in [th.name for th in threading.enumerate()]:
            if "sensors" not in [th.name for th in threading.enumerate()]:
                # Date & Time display
                lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
                lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)
            
        # Stop displaying
        if GPIO.input(15) == GPIO.HIGH or GPIO.input(13) == GPIO.HIGH:
            try:
                clock_thread.join()
            except RuntimeError:
                break

            break
            
        # RESET button
        if GPIO.input(11) == GPIO.HIGH:
            break



if __name__ == "__main__":
    
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    # Set pins to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # SET   GPIO23
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # UP    GPIO22
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # DOWN  GPIO27
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # RESET GPIO17

    lcd = lcddriver.lcd()
    # Possible states: 
    # 0 - Clock Date & Time
    # 1 - Sensors Data
    # 2 - Alarm Set/Alarm Display


    curr_state = 0 # Set 0 as default state
    while True:
        # Use UP and DOWN GPIOs to move between states
        # Arrow UP
        if GPIO.input(15) == GPIO.HIGH:
            print()
            print("Current Threads: ")
            print([th.name for th in threading.enumerate()])
            print(curr_state)
            print("Arrow UP Pressed")

            if curr_state + 1 <= 2:
                curr_state = curr_state + 1
            else:
                curr_state = 0

            print("New state: ")
            print(curr_state)
            print("Current Threads: ")
            print([th.name for th in threading.enumerate()])
            print()

        # Arrow DOWN
        if GPIO.input(13) == GPIO.HIGH:
            print()
            print("Current Threads: ")
            print([th.name for th in threading.enumerate()])
            print(curr_state)
            print("Arrow Down Pressed")

            if curr_state - 1 >= 0:
                curr_state = curr_state - 1
            else:
                curr_state = 2

            print("New state: ")
            print(curr_state)
            print("Current Threads: ")
            print([th.name for th in threading.enumerate()])
            print()
            
        # RESET button
        if GPIO.input(11) == GPIO.HIGH:
            break

        # 0 - Clock Date & Time
        if abs(curr_state) == 0:

            if "clock" not in [th.name for th in threading.enumerate()]:
                print("Starting clock thread...")
                sleep(1)
                clock_thread = threading.Thread(target=clock, name="clock")
                clock_thread.start()
            
        # 1 - Sensors Data
        elif abs(curr_state) == 1:

            if "sensors" not in [th.name for th in threading.enumerate()]:
                print("Starting Sensors thread...")
                sleep(1)
                sensors_thread = threading.Thread(target=display_sensors, name="sensors")
                sensors_thread.start()
            
        # 2 - Alarm Set/Alarm Display
        elif abs(curr_state) == 2:

            #sensors_thread.join()
                
            if "alarm" not in [th.name for th in threading.enumerate()]:
                print("Starting Alarm thread...")
                sleep(1)
                alarm_thread = threading.Thread(target=alarm, name="alarm")
                alarm_thread.start()
        # - Always check sensors

        if True:
            # Sensors measurement
            # Define sensor channels
            light_channel = 1
            temp_channel  = 0

            # Define delay between readings
            delay = 1
            # Read the light sensor data
            light_level = ldr.ReadChannel(light_channel)
            light_volts = ldr.ConvertVolts(light_level, 2)

            # Read the temperature sensor data
            temp_level = ldr.ReadChannel(temp_channel)
            temp_volts = ldr.ConvertVolts(temp_level, 2)
            temp       = ldr.ConvertTemp(temp_volts, 2)

            # Print out results
            print("--------------------------------------------")
            print("Light: {} ({}V)".format(light_level,light_volts))
            print("Temp : {} ({}V) {} C".format(temp_level,temp_volts,temp))

            # Wait before repeating loop
            time.sleep(delay)

    
    
