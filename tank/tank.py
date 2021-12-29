from flask import Blueprint, request, current_app
import RPi.GPIO as GPIO
import time

tank = Blueprint('tank', __name__)

@tank.route('/',methods=['GET'])
def get_level():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    PIN_TRIGGER = 4
    PIN_ECHO = 27

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    # Turn on
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    # Wait to stabilise
    time.sleep(2)

    # Send Trigger
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    # Wait and turn off
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    # Wait for Echo
    while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

    # Convert Echo Time to Distance
    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration * 171500  # in mm
    distance = round(100 * (1 - (distance/135)))  # in %

    return f"{distance}"
