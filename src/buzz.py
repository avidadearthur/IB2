# Libraries
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
from time import sleep

# Disable warnings (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set buzzer - pin as output
buzzer = 32
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # RESET GPIO17

# Buzzer sleep parameters
curr_plus_delta = datetime.now()
curr = datetime.now()
seconds_to_beep = 0

while True:
    curr = datetime.now()
    # get now plus 10 seconds
    curr_plus_delta = curr + timedelta(seconds=2)

    print(seconds_to_beep)
    while seconds_to_beep < 0.5:
        GPIO.output(buzzer, GPIO.HIGH)
        seconds_to_beep = (curr_plus_delta - datetime.now()).total_seconds()

    while seconds_to_beep > 0.5:
        GPIO.output(buzzer, GPIO.LOW)
        seconds_to_beep = (curr_plus_delta - datetime.now()).total_seconds()

    seconds_to_beep = (curr_plus_delta - datetime.now()).total_seconds()

    # RESET button
    if GPIO.input(11) == GPIO.HIGH:
        GPIO.output(buzzer, GPIO.LOW)
        break
