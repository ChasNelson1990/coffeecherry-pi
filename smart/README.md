# The CoffeeCherry Pi `smart`

This directory contains the codes and instructions for setting up the CoffeeCherry Pi for turning the espresso machine on and off.
For the Gaggia Classic, this gives us the ability to flip the ON/OFF switches from our Home Assistant frontend.

The aim is to convert the machine from the mechanical switch:

![The Gaggia Classic circuit controlled by the mechanical ON switch.](./assets/normal.svg)

To a relay connect to the CoffeeCherry Pi GPIOs and controlled by the Home Assistant server:

![The Gaggia Classic circuit controlled by the CoffeeCherry Pi GPIO pins.](./assets/smart.svg)

We're going to do this by connecting the SSR input to a ground pin (e.g. pin 14) and GPIO 18 (i.e. pin 12), which has PWM output and should be able to drive at 3.3 V.
The SSR output can then be connected between the mains live and the brew thermostat (missing the ON switch entirely).

Later, when we add our own thermal probe (`pid` and onwards) we will skip the thermostats completely and connect the SSR output between the mains and straight to the boiler.
When we do this we will also discuss the SSR switiching to get finer control of the boiler, for now we have on and off.

## CoffeeCherry Pi Dependencies

`coffeecherry`

## Bill of Materials

* Solid State Relay (e.g. RS Stock No. 715-0846) - any SSR capable of dealing with your supply voltage (e.g. 240V in the UK), a 3 V control voltage and a suitable current load (e.g. a 25 A SSR)

Note: this assumes that you have a functioning Home Assistant server already running (and that you've already followed the dependency instructions).

## Pins Used

* PWM0 pin, e.g. GPIO 18 or 12 (Board Pin No. 12 or 32, respectively), for live (+ve)
* Ground pin, e.g. Board Pin No. 6, for neutral (-ve)

## Instructions

### Tests

Before we connect all the dangerous thing together, I tested this stage worked by connecting an LED to the pins I was going to use.
By turning the CoffeeCherry Pi on and off I was able to control the LED.
I also measured the output voltage of my pins with a multimeter to confirm that the output was >3 V.

### Codes

* `smart.py` contains the Flask blueprint for this feature, which is registered by the main `coffeecherry.py` code.
* `smart.yaml` contains the Home Assistant configuration YAML for creating a button which can read and set the SSR (i.e. pin 12) state.
  * This must be manually included in your `configuration.yaml`.

### Wiring

First, connect ring or fork termini to two logic wires that have female headers at the other end.
These wires will connect our GPIO pins to the SSR.
Note: you can actually plug the SSR in to the Raspberry Pi with no connection to the mains), press the button in your Home Assistant and you should see the Input LED turn on and off on the SSR.

Then connect ring/fork termini to two high temperature wires and female spade termini to the other ends.
These wires will connect the SSR between the mains (live) and the brew thermostat, replacing the wire coming from the ON switch (middle).

## Results

In order to check my boiler was heating up, I temporarily replaced the steam thermostat with the thermal probe I will be using for the PID.

These are my boiler temperatures when flicking the ON switch before the modifications:

These are my boiler temperatures when toggling the Home Assistant button after the modifications:
