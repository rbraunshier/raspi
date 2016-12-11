import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if(GPIO.input(18) ==1):
        print("Button pressed")
GPIO.cleanup()
