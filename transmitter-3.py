#!/usr/bin/env python3
from time import sleep
import RPi.GPIO as GPIO
import argparse
import logging

from rpi_rf import RFDevice

def transmit(inputval):
    logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

    code = inputval
    protocol=1
    pulselength = 350
    rfdevice = RFDevice(17)  #gpio number
    rfdevice.enable_tx()

    logging.info(str(code) +
                 " [protocol: " + str(protocol) +
                 ", pulselength: " + str(pulselength) + "]")

    rfdevice.tx_code(code, protocol, pulselength)
    rfdevice.cleanup()


GPIO.setmode(GPIO.BCM)
sleepTime = .01
buttonPin = 18  #gpio number
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        input_state = GPIO.input(buttonPin)
        if input_state == False:
            transmit(8888)
            sleep(sleepTime)
        if input_state == True:
            transmit(7777)
            sleep(sleepTime)
               
finally:
    GPIO.cleanup()

