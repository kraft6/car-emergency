#!/usr/bin/env python3
import argparse
import signal
import sys
import time
import logging

from time import sleep
import RPi.GPIO as GPIO
from rpi_rf import RFDevice

def chg_greenlight(parm):
    GPIO.setup(lightGreenPin, GPIO.OUT)
    GPIO.output(lightGreenPin, parm)
    
def chg_redlight(parm):
    GPIO.setup(lightRedPin, GPIO.OUT)
    GPIO.output(lightRedPin, parm)

def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO pin of component
lightGreenPin = 4
lightRedPin = 21

rfdevice = None

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))

while True:
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        #print (rfdevice.rx_code)
        if rfdevice.rx_code == 8888:
            chg_greenlight(False)
            chg_redlight(True)
        elif rfdevice.rx_code == 7777:
            chg_redlight(False)
            chg_greenlight(True)
        else:
            continue
            
        logging.info(str(rfdevice.rx_code) +
                     " [pulselength " + str(rfdevice.rx_pulselength) +
                     ", protocol " + str(rfdevice.rx_proto) + "]")
    time.sleep(0.01)

rfdevice.cleanup()
  

