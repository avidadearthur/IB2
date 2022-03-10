# Libraries
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
from time import sleep

# Disable warnings (optional)
GPIO.setwarnings(False)
# Set buzzer - pin as output
buzzer = 32
GPIO.setup(buzzer, GPIO.OUT)

# Buzzer sleep parameters
curr_plus_delta = datetime.now()
curr = datetime.now()
seconds_to_beep = 0

while True:
    if seconds_to_beep < 0:
        GPIO.output(buzzer, GPIO.HIGH)
        curr = datetime.now()
        # get now plus 10 seconds
        curr_plus_delta = curr + timedelta(seconds=0.5)
    elif seconds_to_beep < -0.5:
        GPIO.output(buzzer, GPIO.LOW)

    seconds_to_beep = (curr_plus_delta - datetime.now()).total_seconds()

    # RESET button
    if GPIO.input(11) == GPIO.HIGH:
        GPIO.output(buzzer, GPIO.LOW)
        break
