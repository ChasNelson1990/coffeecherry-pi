# The CoffeeCherry Pi `pid`

This directory contains the codes and instructions for setting up the CoffeeCherry Pi to control boiler temperature using a pid system.

## CoffeeCherry Pi Dependencies

`smart`

## Bill of Materials

* Temperature sensor (RS Stock No. 133-0679) - any temperature sensor will do remember that a) it needs to be able to deal with high temperatures for steam mode (so 150 C or up) and the better the accuracy/resolution the more stable your boiler.
* M4 spacer (RS Stock No. 161-3636) - essentially we're stealing James' idea from this post http://int03.co.uk/blog/2014/04/16/replacing-the-gaggia-classic-coffee-thermostat-with-a-tsic-306/

Note: this assumes that you have a functioning Home Assistant server already running (and that you've already followed the dependency instructions).

## Pins Used

* 3.3 V pin, i.e. Board Pin No. 1, for Vcc for the temperature probes
  * Note: we can power both temperature probes from the same pin
* Ground pin, e.g. Board Pin No. 14, for ground for the temperature probes
  * Note: again, both temperature probes will share the same ground pin
* 2x GPIO pins, e.g. GPIO 17 and 22 (Board Pin No. 11 and 15, respectively), for the temperature probe signals

## Instructions

### PID v1

For PID v1, I have essentially just adapted the algorithm available here: https://github.com/esrice/piggia/.

1. The temperature probes have three wires: one for Vcc, one for ground and one for signal. I soldered long, headed wires to these and a small 100 nF capacitor between the Vcc and ground pins. I then insulated each wire and the capacitor with electricians tape (heat shrink would have been better)
2. Connect the two temperature probes as per the pins above - you can check they work by warming the probes up between your fingers.
3. Drill a bigger hole into the M4 spacers so that your temperature probes can be pushed to the bottom.
4. Fill the hole with thermal paste/grease, insert the termperature probe and seal the unit with heat shrink.
5. Replace the existing thermosistors with the new temperature probes.
6. Move the connection from the `smart` module SSR (the one that goes from the SSR live to the brew thermostat) so that it now goes directly to the boiler, thus skipping both of the prebuilt thermostats (which we've removed from position).

### Results

Whilst testing this I replaced just the steam thermostat and disconnected the SSR (returning to the original wiring), turned the machine on and logged the temperature of my steam temperature probe in normal mode:

I then put the steam thermostat back but replaced the brew thermostat with a temperature probe and repeated:

This meant I knew exactly how my temperature probes related to the termostats and what temperatures I was aiming for and how bad the default stability really is.

I then repeated this but using the PID algorithm for a brew temperature:

And for a steam temperature:

