# The CoffeeCherry Pi `smart`

This directory contains the codes and instructions for setting up the CoffeeCherry Pi for turning the espresso machine on and off.
For the Gaggia Classic, this gives us the ability to flip the ON/OFF switches from our Home Assistant frontend.

The aim is to convert the machine from the mechanical switch:

![The Gaggia Classic circuit controlled by the mechanical ON switch.](./assets/normal.svg)

To a relay connect to the CoffeeCherry Pi GPIOs and controlled by the Home Assistant server:

![The Gaggia Classic circuit controlled by the CoffeeCherry Pi GPIO pins.](./assets/smart.svg)

## CoffeeCherry Pi Dependencies

`coffeecherry`

## Bill of Materials

* Solid State Relay (e.g. RS Stock No. 715-0846) - any SSR capable of dealing with your supply voltage (e.g. 240V in the UK), a 3 V control voltage and a suitable current load (e.g. a 25 A SSR)

Note: this assumes that you have a functioning Home Assistant server already running (and that you've already followed the dependency instructions).

## Instructions

