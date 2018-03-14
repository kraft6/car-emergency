#Test Project
from time import sleep
import RPi.GPIO as GPIO
print('Reciver')

GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO pin of component
lightPin = 4
buttonPin = 17


GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)

try:
    while True:
        GPIO.output(lightPin, not GPIO.input(buttonPin))
        sleep(.1)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()
            
                
#GPIO.output(4, True)
#time.sleep(1)
#GPIO.output(4, False)



