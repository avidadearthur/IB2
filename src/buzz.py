# Libraries
import RPi.GPIO as GPIO
from time import sleep

# Disable warnings (optional)
GPIO.setwarnings(False)
# Select GPIO mode
GPIO.setmode(GPIO.BCM)
# Set buzzer - pin as output
buzzer = 12
GPIO.setup(buzzer, GPIO.OUT)


def set_buzz(beep=True):
    while beep:
        GPIO.output(buzzer, GPIO.HIGH)
        print("Beep")
        sleep(0.5)  # Delay in seconds
        GPIO.output(buzzer, GPIO.LOW)
        print("No Beep")
        sleep(0.5)
