from flask import Blueprint, request, current_app
import RPi.GPIO as GPIO

smart_ssr = Blueprint('smart_ssr', __name__)

@smart_ssr.route('/',methods=['GET'])
def get_state():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)

    current_state = GPIO.input(18)

    if current_state:
        return 'on'
    elif not current_state:
        return 'off'

@smart_ssr.route('/',methods=['POST'])
def set_state():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)

    desired_state = request.data.decode('UTF-8')
    if desired_state=='on':
        GPIO.output(18,GPIO.HIGH)
    if desired_state=='off':
        GPIO.output(18,GPIO.LOW)

    return desired_state
