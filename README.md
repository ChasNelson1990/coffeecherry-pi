# The CoffeeCherry Pi

![CoffeeCherry Pi Logo](coffeecherry-pi.svg)

## Making a semi-automatic espresso machine fully automatic

This is a personal project to build a Raspberry Pi-based system for automatically profiling and allowing full digital control of a Gagglia Classic semi-automatic espresso machine.
I have given it the, oh so witty, name of the CoffeeCherry Pi.

## Background

It was a dark and stormy night, the moon was full and I lay there dreaming, unable to sleep.
I had had too much coffee.
As I lay there tossing and turning I remembered the flat whites I had drunk from my recently purchased, second-hand Gaggia Classic espresso machine.
One had extracted slowly, the espresso had a thick crema and a full body - it had made a lovely morning coffee.
The other was lacklustre with a rapidly dissapearing crema resulting in a flat and sour coffee that was a challenge to drink.
The difference between these two coffees - a error between the ~screen~ cup and the ~keyboard~ buttons.
So, I decided to remove that error, i.e. me, from as much of my espresso making process as possible.

Luckily, one of the reasons I had purchased a Gaggia Classic in the first place was that there is a large modding community to be found on all forums.
I spent many a day when I should have been working (during the CoViD-19 lockdown) reading forum posts and GitHub projects.
Although there were many add-ons I could purchase or open-source solutions I could make myself, none of them did everything I wanted in one easy-to-get and easy-to-use package.
So, I decided to start from scratch.
I decided to build a system, the CoffeeCherry Pi, that had all the features I desired and none of those that I didn't (see Features and Rationale below).

This repository is my attempt to document the CoffeeCherry Pi in an easy-to-share way.
I hope somebody other than me finds it useful (and I will respond to Issues people raise [as quickly as I can]).

## Rationale

The CoffeeCherry Pi system has been developed with the following five philosophies.

1. **Open-source** - all of the hardware and software choices I make should be driven by the guiding principle of 'open' (let's iggnore the Raspberry Pi itself...).
2. **Available** - but more than this, many of the open source projects I found required the ability to build (or buy from the creators) PCB boards (and often they had sold out), so this project will only use components that can be easily purchased or alternatives quickly identified and whilst soldering may be required, PCB creation is not*.
3. **Data-driven** - I am a data geek, it's my job(s), I spend a lot of spare time reading/thinking about/analysing data, any feature that I add to the system should enable me to first log or profile a characteristic of my extraction and then, second, control that characteristic (ideally in an automated way).
4. **Smart** - this might seem obvious for an automatic machine, but I mean 'smart' as in 'smart home'; I designed this project to be integrated into my home automation system (I, for a variety of reasons, currently use https://www.home-assistant.io/).
5. **Non-destructive** - although I doubt I'll ever sell my Gaggia Classic (unless I come into a lot of money and buy something well fancy) I want that option - all of my added features should do no (or very little) damage to the original Gaggia Classic, i.e. if I make this change I should be able to undo it and return to factor settings.

* an additional aspect of this is that I may use 3D printed components here as I beleive if you don't have direct access to a 3D printer there are many services for getting cheap and quick 3D prints done for you.

### Language

CoffeeCherry Pi is written in Python where-so-ever possible; I am a parseltongue.
Some bits may be written in C or C++ speed; this will often be me stealing (and citing) somebody else's excellent work.

## Features

Below is a list of CoffeeCherry Pi [desired] features (in order of suggested implementation).

Note: these choices are based heavily on reading about the other amazing projects and solutions that are out there (see the Bibliography below).

- [ ] `coffeecherry` - a system to ensure all features are correctly loaded on the Raspberry Pi and to control logging.
- [ ] `smart` espresso machine - the ability to control the ON/OFF, STEAM and BREW switches from a HomeAssitant portal (other logging and control features will be accessible from the same portal).
- [ ] Water `tank` fill monitoring - a simple water level sensor system to ensure the tank never runs dry.
- [ ] `pid` temperature control - this is a more efficient and accurate algorithm for controlling the boiler temperature to ensure consistent espresso extraction.
- [ ] Ready `alarm` - a simple alarm to notify you that the system is warmed up and ready to go.
- [ ] Extraction `brew` - automated extraction of a shot (based on time).
- [ ] `recipes` - a simple way to programme in recipes (i.e. extraction temperature and time [and later pressure and more]) that can be re-used and easily modified, i.e. for new beans.
- [ ] `one-push` shot extraction - extract a shot by pressing a single button.
- [ ] Automatic `steam` switch - automatically flip the steam switch after a shot is extracted to speed up the total time to flat white deliciousness.
- [ ] `sleep` - automatically put the machine into a power-save mode when not used for a pre-determined time; this helps to save energy and extend the life of the machine.
- [ ] Cleaning `reminder` - reminder, based on number of extracted shots and number of days since last clean, to 1) backflush and 2) descale the machine.
- [ ] Extraction `volume` - automated measurement and/or control of the extraction volume of a shot.
- [ ] `dial-in` assistant - a calibration process that take an ideal extraction time and volume and helps you 'dial in' your grind size for a new bean.
- [ ] `cupping` - a simple cupping form to [optionally] fill out after each extraction so that we can start to determine the difference between a 'good' and 'bad' extraction based on the logs.
- [ ] `dashboard` - a visualisation dashboard for all logged variables, including cupping.
- [ ] `pressure-profiling` - the ability to measure and/or control the pressure of an extraction extraction; this will allow a range of constant pressure 'recipes', e.g. a flat 13 bars (the factory default), a flat 9 bars (a more accepted default). (See also `preinfusion`.
- [ ] `preinfusion` - more complex pressure 'recipes' that allow a low pressure pre-infusion to saturate the puck and prevent channeling. (See also `pressure-profiling`.)
- [ ] Post-brew `soft-stop` - reduces the pressure gardually at the end of an extraction, preventing coffee from being forced back into the brewhead.
- [ ] `double` boiler power - increased boiler power means a faster heat-up and (I need to confirm this) reduced total elecricity use.
- [ ] `backflush` - an automated backflushing protocol for use with or without detergent to help keep the machine clean.
- [ ] `pid2` - improved temperature control for bringing the system up to temperature quickly based on Tom Brazier's systems.
- [ ] `eink` screen - designed to replace (reversibly) the manual switches so that the user can see the current state of the machine. e.g. temperature, pressure, etc..

## How to use this repository

Each feature has been given it's own directory (with the name matching the highlighted word in the feature list).
Directories contain a readme detailing the feature including dependencies and instructions to implement hardware changes, a bill of materials (see below), any hardware design files (in editable and open file formats) and all codes.
This repository is designed under the assumption that you will be using the core `coffeecherry` feature and interacting with the device through the same home automation system as me.
However, many features will be independent, i.e. you can pick and choose which you add to your system by borrowing chunks of my code or some of the designs.

To start putting together a CoffeeCherry Pi begin with `coffeecherry` and go through the features as ordered on the main repository readme.

There is also a `base` directory, which contains my understanding of the original system; this is mostly for reference but does include a list of recommended tools and 'stock' equipment, e.g. what type of wires to use.

Finally, there is an `additional` folder that contains links to resources for other mods I've made to my machine that aren't part of the CoffeeCherry Pi control system.

### Bills of Material

Where possible my bills of material list components with a manufacturer number and a major supplier code, usually RS, so that you should always be able to source the component.
There are two caveats to this: 1) it may not always be possible, in which case I will list where I sourced the compenent from, and 2) a major supplier may not be the cheapest option (e.g. eBay might be cheaper).
Finally, I will try and justify each component so that you might use alternative components if you can't find the original.

## Bibliography

This is a list of some of the amazing projects and forum threads that I read in developing my ideas for this project.
It is far from complete so if anybody thinks I've accidentally borrowed from somebody without citing them - please let me know via the issues!

* http://espresso-for-geeks.kalaf.net/ - An amazingly detailed resource designed by geeks for modding a semi-automatic espresso machine using and mbed microcontroller; I have no experience in using this and so this wasn't the solutuion for me.
* http://tomblog.firstsolo.net/index.php/hobbies/pimping-my-coffee-machine/ - Another amazingly detailed resource which is started from an Arduino-based PID but includes a lot more and is the inspiration for the `pid2` feature.
* http://int03.co.uk/blog/project-coffee-espiresso-machine/ - A Raspberry Pi-based system that incorporates many of the features listed above with a fancy little LCD screen and a couple of buttons for operation.
* http://www.cyberelectronics.org/?p=458 - Another Arduino system, I mostly used this as inspiration for features.
* https://protofusion.org/wordpress/2019/02/gaggia-classic-seamless-pid-upgrade/ - Instructions for using the open source Therm PID controller.
* https://coffeeforums.co.uk/ - I learnt a lot by reading the threads on Coffee Forums and I'm sure I'll be adding specific threads and users here as the project grows.


## Disclaimer

Oh, and, of course, making changes to any espresso machine will probably void you warranty and is definitely dangerous.
You're dealing with mains power electricity and with hot, boiling water and steam - do not make any of these changes if you are not confident in managing the risks associated.
I take no liability if things go wrong.
