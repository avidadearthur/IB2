#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep, strftime
from datetime import datetime, timedelta

import lcddriver
import sensors
import threading
import RPi.GPIO as GPIO

# Dictionary of alarms
global ALARMS

ALARMS = {}
# ALARMS = { "24/02": ["06:00", "06:30"], "25/02": ["07:00", "07:30"], ... }
ALARMS.update({"28-02": ["07:00", "07:30"]})


def display_alarm():
    lcd.lcd_clear()

    while True:

        if "clock" not in [th.name for th in threading.enumerate()]:
            if "sensors" not in [th.name for th in threading.enumerate()]:
                # Code for the alarm goes here

                # Date & Time display
                tomorrow = datetime.now() + timedelta(days=1)
                tomorrow_str = tomorrow.strftime('%d-%m')

                lcd.lcd_display_string('Nxt Alarm: {}'.format(ALARMS[tomorrow_str][0]), 1)
                lcd.lcd_display_string(tomorrow.strftime('%a, %b %d %Y'), 2)

                # Arrow SET
                if GPIO.input(16) == GPIO.HIGH:
                    # Prepare for new display
                    lcd.lcd_clear()

                    edit_mode = True

                    # Convert dictionary str vale to int
                    time_str = ALARMS[tomorrow_str][0]
                    hour = int(time_str[0:2])
                    minute = int(time_str[3:])
                    alarm_day = tomorrow  # Assume for now that we can only alter tomorrow's 1st alarm

                    # Possible states:
                    change_hour = True  # start by changing the hour field by default
                    change_minutes = False

                    while edit_mode:

                        while change_hour:

                            lcd.lcd_display_string('Nxt Alarm: {:02}:{:02}'.format(hour, minute), 1)
                            # Assume for now that we can only alter tomorrow's 1st alarm
                            lcd.lcd_display_string(alarm_day.strftime('%a, %b %d %Y'), 2)

                            # Leave change_hour and go to change_minutes:
                            if GPIO.input(16) == GPIO.HIGH:
                                change_hour = False
                                change_minutes = True

                            else:
                                # Use UP and DOWN GPIOs to INCREMENT/DECREMENT value
                                # Arrow UP
                                if GPIO.input(15) == GPIO.HIGH:
                                    if hour < 24:
                                        hour += 1

                                # Arrow DOWN
                                if GPIO.input(13) == GPIO.HIGH:
                                    if hour > 0:
                                        hour -= 1

                        while change_minutes:

                            lcd.lcd_display_string('Nxt Alarm: {:02}:{:02}'.format(hour, minute), 1)

                            # Assume for now that we can only alter tomorrow's 1st alarm
                            lcd.lcd_display_string(alarm_day.strftime('%a, %b %d %Y'), 2)

                            # Leave edit mode:
                            if GPIO.input(16) == GPIO.HIGH:
                                change_hour = True
                                change_minutes = False
                                edit_mode = False

                                # Update ALARM Dict
                                updated_list = [time for time in ALARMS[tomorrow_str]]

                                updated_list[0] = '{:02}:{:02}'.format(hour, minute)
                                ALARMS[tomorrow_str] = updated_list

                            else:
                                # Use UP and DOWN GPIOs to INCREMENT/DECREMENT value
                                # Arrow UP
                                if GPIO.input(15) == GPIO.HIGH:
                                    if minute < 59:
                                        minute += 1

                                # Arrow DOWN
                                if GPIO.input(13) == GPIO.HIGH:
                                    if minute > 0:
                                        minute -= 1

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
    lcd.lcd_clear()

    while True:

        if "clock" not in [th.name for th in threading.enumerate()]:
            if "alarm" not in [th.name for th in threading.enumerate()]:
                lcd.lcd_display_string('Sensors Data', 1)
                # Code for the sensors
                # Define sensor channel
                temp_channel = 0

                # Read the temperature sensor data
                temp_level = sensors.ReadChannel(temp_channel)
                temp_volts = sensors.ConvertVolts(temp_level, 2)
                temp = sensors.ConvertTemp(temp_volts, 2)

                # Print out results to lcd screen
                lcd.lcd_display_string("Temp : {} C".format(temp), 2)

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


def display_clock():
    # Always start by clearing the LCD
    lcd.lcd_clear()

    while True:

        if "alarm" not in [th.name for th in threading.enumerate()]:
            if "sensors" not in [th.name for th in threading.enumerate()]:
                # Date & Time display
                lcd.lcd_display_string(strftime('TIME: ' '%H:%M:%S'), 1)
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

    GPIO.setwarnings(False)  # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

    # Set pins to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # SET   GPIO23
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # UP    GPIO22
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # DOWN  GPIO27
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # RESET GPIO17

    # Set output pins
    GPIO.setup(36, GPIO.OUT, initial=0)  # LEDs  GPIO16

    lcd = lcddriver.lcd()
    # Possible states: 
    # 0 - Clock Date & Time
    # 1 - Sensors Data
    # 2 - Alarm Set/Alarm Display

    curr_state = 0  # Set 0 as default state
    while True:
        # Use UP and DOWN GPIOs to move between states
        # Arrow UP
        if GPIO.input(15) == GPIO.HIGH:
            if "alarm" not in [th.name for th in threading.enumerate()]:
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
            if "alarm" not in [th.name for th in threading.enumerate()]:
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
                sleep(0.2)
                clock_thread = threading.Thread(target=display_clock, name="clock")
                clock_thread.start()

        # 1 - Sensors Data
        elif abs(curr_state) == 1:

            if "sensors" not in [th.name for th in threading.enumerate()]:
                print("Starting Sensors thread...")
                sleep(0.2)
                sensors_thread = threading.Thread(target=display_sensors, name="sensors")
                sensors_thread.start()

        # 2 - Alarm Set/Alarm Display
        elif abs(curr_state) == 2:

            # sensors_thread.join()

            if "alarm" not in [th.name for th in threading.enumerate()]:
                print("Starting Alarm thread...")
                sleep(0.2)
                alarm_thread = threading.Thread(target=display_alarm, name="alarm")
                alarm_thread.start()

        # X - Always check for the next alarm
        # count down and database push/pull code will probably come here

        # X - Always check ldr

        # Define sensor channels
        light_channel = 1

        # Read the light sensor data
        light_level = sensors.ReadChannel(light_channel)
        light_volts = sensors.ConvertVolts(light_level, 2)

        # Define LED states
        if light_volts > 2.0:
            GPIO.output(36, 1)
        else:
            GPIO.output(36, 0)
