# The CoffeeCherry Pi `brew`

This directory contains the codes and instructions for setting up the CoffeeCherry Pi for turning the espresso machine pump on for a timed period and off, i.e. a basic extraction.
For the Gaggia Classic, this gives us the ability to flip the BREW switch from our Home Assistant frontend; the switch automatic flips back after the set time.

The aim is to convert the machine from it's original mechanical switch:

![The Gaggia Classic circuit controlled by the mechanical BREW switch.](./assets/normal.svg)

To a relay connect to the CoffeeCherry Pi GPIOs and controlled by the Home Assistant server:

![The Gaggia Classic circuit controlled by the CoffeeCherry Pi GPIO pins.](./assets/smart.svg)

Essentially, this is the same as we did in `smart` but for on/off control of the pump. Later on we will upgrade this so that we can actually control the pumping rate and not just on/off.

## CoffeeCherry Pi Dependencies

`coffeecherry`, `smart`

## Bill of Materials

* Solid State Relay (e.g. RS Stock No. 715-0846) - any SSR capable of dealing with your supply voltage (e.g. 240V in the UK), a 3 V control voltage and a suitable current load (e.g. a 25 A SSR)

Note: this assumes that you have a functioning Home Assistant server already running (and that you've already followed the dependency instructions).

## Instructions

