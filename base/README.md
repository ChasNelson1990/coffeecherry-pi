# The CoffeeCherry Pi `base`

This directory is for keeping information about my **Gaggia Classic** and how it should work/be constructed.
The main aim of this is so that I have a reference (including photographs) of how to undo any mods I make - and also to make me think hard before doing anything.

## Schematics

### Parts diagram

Link: https://wiki.wholelattelove.com/images/6/6a/CLASSIC_Parts_Diagram.pdf

However, it's often easier to remind myself of the simple design of the Gaggia Classic:

![A simplistic sketch of the Gaggia Classic's components.](./assets/sketch.svg)

### Wiring diagrams

Link: https://wiki.wholelattelove.com/images/a/aa/CLASSIC_Electrical_Diagram.pdf

I found the complete wiring diagram a bit difficult to navigate at first so ended up sketching out the circuits for each switch state.
This made things clear for me at least.

#### ON State

These are the complete circuits when the machine is switched on (at the ON/OFF switch) but the STEAM and BREW switches are left off.
Essentially, in this state two parallel circuits are on: 1) the ON/OFF light and 2) the heating element.
The heating element circuit comprises two thermostats: the coffee thermostat, which trips at 107 C, and the steam thermostat, which trips at 145 C.
Because the coffee thermostat trips at a lower temperature, in this mode the heating elements will be on when the thermostat registers less than 107 C and will be automatically turned off when the thermostat registers 107 C.

Note: my positioning of the the brew light follows the above official schematic; however, I don't think that makes sense.
Given that the light is on when the heating elements are on and off otherwise, I think, and I may be wrong, that the brew light is actually wired after the thermostats and in parallel to the heating element.

![Completed circuits when the Gaggia Classic is in the ON state.](./assets/on.svg)

#### BREW State

These are the complete circuits when the machine is switched on at the ON/OFF switch and the BREW switch is also on (but the STEAM switch is off).
In this state two additional circuits are activated: 1) the pump, which pumps cold water from the tank into the boiler and thus forces hot water out of the boiler and 2) the solenoid valve, which in this state directs the hot water into the brew head.

![Completed circuits when the Gaggia Classic is in the BREW state.](./assets/brew.svg)

#### STEAM State

These are the complete circuits when the machine is switched on at the ON/OFF switch and the STEAM switch is also on (but the BREW switch is off).
The only difference between this and the ON state is that a small circuit bypasses coffee thermostat meaning that the boiler will now heat up until the 145 C steam thermostat trips, which ensures there is high pressure steam inside the boiler.
When you then open the steam valve this steam goes through the steam wand.

![Completed circuits when the Gaggia Classic is in the BREW state.](./assets/steam.svg)

#### STEAM+BREW State

These are the complete circuits when the machine is switched on at the ON/OFF switch and the STEAM and BREW switches are also on.
I think this state is only used for priming the machine when you first set it up.
It is the same as the STEAM state, i.e. using the higher temperature thermostat, but also keeps the pump on.
Because the solenoid is still closed water can't go through the brew head.
When the steam valve is opened then steam rushes through the wand but is quickly replaced by the water being pumped into the boiler and so eventually get a solid stream of water from the steam wand.

![Completed circuits when the Gaggia Classic is in the STEAM+BREW state.](./assets/steam-brew.svg)

## Recommended Tools

For the mods described in this repository you will need the following tools and 'stock' products.

* High-temperature wire (e.g. RS Stock No. 724-4496) - this is the important wire, must be capable of carrying mains voltage and be able to deal with the currents being drawn by the boiler.
* Any old wires (e.g. RS Stock No. 120-9208) - this wire is less important and will be used for connecting the Raspberry Pi to sensors and switches.
* Heat shrink tubing (e.g. RS Stock No. 170-6298) - this shrink wrap is pretty comfortable at high temperatures and is used to protect connections and soldering joints or also just to give an extra layer of protection to wires near the boiler.
* Spade connectors (e.g. RS Stock No. 534-828) - you can't solder wires to the boiler (because it's to hot) so we'll use crimp spade connectors for most of our junctions, get a box set. Note: colour indicates width.

Note: you will also need access to a 3D printer. If you don't have a 3D printer there are many services online that are cheap and quick.