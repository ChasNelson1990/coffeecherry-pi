from flask import Blueprint, request, current_app
import RPi.GPIO as GPIO

import pigpio
from tsic import TsicInputChannel, Measurement, TSIC306
import time

import multiprocessing


def run(ssr_pin, temperature_pin, desired_temperature, K_p=4, K_i=0.01, K_d=0, max_integral=2500, max_error_accumulation=10,
        delay_time=1, frequency=1):
    """
    Modified from https://github.com/esrice/piggia/.
    Implements a proportional-integral-derivative
    controller, which intelligently modifies the
    pulse width of the boiler to keep the temperature
    from swinging too much.
    Arguments:
    * ssr_pin: the GPIO pin controlling the relay, in
        BCM numbering
    * thermometer: a Thermometer instance
    * desired_temperature: the temperature to aim for, in deg C
    * K_p, K_i, K_d: the PID controller constants for the
        proportional, integral, and derivative terms,
        respectively.
    * max_integral: maximum value integral term is allowed
      to reach, to prevent integral windup
    * max_error_accumulation: maximum abs(error), in
      degrees C, under which integral term is allowed to
      accumulate
    * delay_time: time between readings, in seconds
    * frequency: frequency of PWM, in Hz
    """

    def read_temp():
        pi = pigpio.pi()
        tsic = TsicInputChannel(pigpio_pi=pi, gpio=temperature_pin, tsic_type=TSIC306)
        measurement = tsic.measure_once(timeout=1.0)
        pi.stop()
        if not (measurement == Measurement.UNDEF):
            return measurement.degree_celsius

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(ssr_pin,GPIO.OUT)

    pwm = GPIO.PWM(ssr_pin, frequency)
    pwm.start(0)

    previous_integral = 0.0
    previous_error = 0
    previous_time = time.time()
    while True:
        current_temperature = read_temp()
        current_time = time.time()

        if current_temperature is not None:
            # calculate the proportional, integral, and derivative terms
            error = desired_temperature - current_temperature
            delta_t = current_time - previous_time
            derivative = (error - previous_error) / delta_t

            integral = previous_integral + 0.5 * (error + previous_error) * delta_t
            if integral > max_integral:
                integral = 0
            if abs(error) > max_error_accumulation:
                integral = previous_integral
            if current_temperature < 80:
                integral = 0

            # calculate the output and set boiler
            new_duty_cycle = K_p * error + K_i * integral + K_p * derivative
            # confine duty cycle in range [0,100]
            new_duty_cycle = max(0, min(new_duty_cycle, 100))
            pwm.ChangeDutyCycle(new_duty_cycle)

            # keep track of current terms for next cycle through loop
            previous_integral = integral
            previous_error = error
            previous_time = current_time

            time.sleep(delay_time)


def clean_shutdown(ssr_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(ssr_pin,GPIO.OUT)
    GPIO.output(ssr_pin,GPIO.LOW)
    GPIO.cleanup(ssr_pin)


def new_pid(pin, temperature):
    pid = Blueprint(f'pid_{temperature}', __name__)


    @pid.route('/temperature',methods=['GET'])
    def read_temp():
        pi = pigpio.pi()
        tsic = TsicInputChannel(pigpio_pi=pi, gpio=pin, tsic_type=TSIC306)
        measurement = tsic.measure_once(timeout=1.0)
        pi.stop()
        if measurement == Measurement.UNDEF:
            return "-273.15"
        else:
            return f"{round(measurement.degree_celsius, 2)}"


    @pid.route('/', methods=['GET'])
    def check_pid():
        for p in multiprocessing.active_children():
            if p.name=="PID":
                return 'on'
        return 'off'


    @pid.route('/', methods=['POST'])
    def brew_pid():
        desired_state = request.data.decode('UTF-8')
        if desired_state=='on':
            for p in multiprocessing.active_children():
                if p.name=="PID":
                    current_app.logger.warning('Terminating existing PID.')
                    p.terminate()
                    clean_shutdown(18)
            multiprocessing.Process(target=run, args=(18, pin, temperature), name='PID').start()
        if desired_state=='off':
            for p in multiprocessing.active_children():
                if p.name=="PID":
                    current_app.logger.warning(f'Terminating {p.name} on request.')
                    p.terminate()
                    clean_shutdown(18)

        return desired_state

    return pid