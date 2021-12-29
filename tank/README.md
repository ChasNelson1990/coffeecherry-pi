# The CoffeeCherry Pi `tank`

This directory contains the codes and instructions for setting up the CoffeeCherry Pi for monitoring the tank fill level from the Home Assistant frontend.

## CoffeeCherry Pi Dependencies

`smart`

## Bill of Materials

* Ultrasonic range finder (RS Stock No. 781-0942 [dev kit]) - the actual board is the HC-SR04 distance ranging board.
* Two resistors with resistances of ratio of 2:3, e.g. I used 220 Ohm and 330 Ohm - this is used to create a potential divider so we can use 3.3 V GPIO pins.

Note: this assumes that you have a functioning Home Assistant server already running (and that you've already followed the dependency instructions).

## Pins Used

* Either 5 V pin, e.g. Board Pin No. 4, for Vcc
* Any GPIO pin, e.g. GPIO 4 (Board Pin No. 7), for trigger
* Any GPIO pin, e.g. GPIO 27 (Board Pin No. 13), for echo
* Ground pin, e.g. Board Pin No. 9

## Instructions

Basically, follow this tutorial: https://pimylifeup.com/raspberry-pi-distance-sensor/.

Differences: use `GPIO.setmode(GPIO.BCM)` for consistency with our other GPIO modules, use `PIN_TRIGGER = 4` (Pin No. 7) and `PIN_ECHO = 27` (Pin No. 13) and connect the ground to Pin No. 9 and the Vcc to Pin No. 4.