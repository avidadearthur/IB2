import gpiozero

out = gpiozero.PWMOutputDevice(12)


while True:
    out.frequency = 10000
    out.value = 0.5
    #ss