# Libraries
import RPi.GPIO as GPIO
from time import sleep

# Disable warnings (optional)
GPIO.setwarnings(False)
# Select GPIO mode
GPIO.setmode(GPIO.BOARD)
# Set buzzer - pin as output
buzzer = 32
GPIO.setup(buzzer, GPIO.OUT)

while True:
    GPIO.output(buzzer, GPIO.HIGH)
    print("Beep")
    sleep(1)  # Delay in seconds
    GPIO.output(buzzer, GPIO.LOW)
    print("No Beep")
    sleep(1)
