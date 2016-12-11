import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def printFunction(channel):
    print("Button pressed!")
    print("***************")

GPIO.add_event_detect(18, GPIO.RISING, callback=printFunction, bouncetime=3000)

