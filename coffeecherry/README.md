# The CoffeeCherry Pi `coffeecherry`

This directory contains the codes and instructions for setting up a Raspberry Pi for a CoffeeCherry Pi instance.

## CoffeeCherry Pi Dependencies

None.

## Bill of Materials

* Raspberry Pi 4 Model B 4 GB (RS Stock No. 182-2096) - in theory this could be any Raspberry Pi or similar computer but I had one of these to hand when I started the project.
* SanDisk 16 GB MicroSD SD Card (RS Stock No. 121-3897) - 16 GB is probably overkill but it's likely the size that will come in a bundle. If you get one with NOOBS pre-installed this will make your life easier, particularly if you're new to the Pi.
* Raspberry Pi Power Supply (RS Stock No. 187-3416) - if you're new to Raspberry Pi, please buy the official power supply (which usually comes in any bundle) because the USB-C socket on the new Pi 4s can easily overheat with the wrong power supply and your Pi will keep shutting itself down because of this. Note: In a later version I will replace the need for this by integrating an AC adapter into the espresso machine and powering the Raspberry Pi through the GPIO pins.

Note: for setting the Raspberry Pi up you will also need a monitor, a micro-HDMI cable, a keyboard and mouse.

Important: I have not included any of the official cases because a) they leave open all the ports, e.g. ethernet, which we won't use and b) they don't leave open easy access to the GPIO pins.
I intend to design a case that does the opposite for 3D printing as I want to minimise openings (for water protection).
For now, use any case but just be careful to keep the case away from any water.

## Pins Used

None.

## Instructions

### Install Raspberry Pi OS

I am not going to go through the details of setting up a Raspberry Pi.
If you're completely new to Raspberry Pis I suggest you follow this tutorial: https://magpi.raspberrypi.org/articles/set-up-raspberry-pi-4.
If you're comfortable with Raspberry Pis then set one up with the latest Raspberry Pi OS; I used the 32-bit version with desktop and default software just for ease.

Be sure to set-up your timezone, language and WiFi connection.

Don't change the default username from `pi` (but do change the password).

### `raspi-config`

With the Raspberry Pi set-up we need to configure a few features.
This is easiest todo with the monitor, keyboard and mouse still connected.
Either run the configuration tool from the user interface or open a terminal and run `sudo raspi-config`.
If you're new to `raspi-config` read this page: https://www.raspberrypi.org/documentation/configuration/raspi-config.md.

1. We need to set the hostname so we can easily access the Pi from the network, I suggest `coffeecherry` and will use this for all of my set-ups.
2. We need to enable SSH so that we can log-in remotely and update the system or debug problems.
3. If you're not use to the command line and SSH then you could turn on and set-up the VNC interface - I will not write anymore about this.
4. As I won't use the graphical interface I have also set the boot options to load straight into command line.
5. While you're in the boot options, ensure that the boot waits for the network to be available as we need that for communicating between the CoffeeCherry Pi and the main Home Assistant server.

### Clone CoffeeCherry Pi onto the Raspberry Pi

Open a terminal and clone this repository onto your new and set-up Raspberry Pi.
Using `cd ~; git clone git@github.com:ChasNelson1990/coffeecherry-pi.git` will clone the repository to the Raspberry Pi default user's home folder - this is where we want it.

### Customising Your CoffeeCherry Pi

Essentially CoffeeCherry Pi runs a Flask-RESTful server that our Home Assistant instance can interact with over the network.
I've designed it using Flask blueprints that are included in the server by including a line like the following in `coffeecherry.py`:
```app.register_blueprint(smart).```
If there's a feature you don't want - comment that line out.

### Install CoffeeCherry Pi (and dependencies)

The `install.py` script moves files that need to be moved and starts a systemd service that runs the server on boot.
The `requirements.txt` file (in the root folder) lists the dependencies.

Run the following to do everything: `cd ~/coffeecherry-pi; python3 -m pip install -r requirements.txt; cd ./coffeecherry/; python3 install.py install`.

### Updating CoffeeCherry Pi

To update your CoffeeCherry Pi when there's a new release log into your Raspberry Pi (either via SSH/VNC or by connecting it to a monitor) and run the following commands: `cd ~/coffeecherry-pi; git pull; python3 -m pip install -r requirements.txt; cd ~/coffeecherry-pi/coffeecherry/; python3 install.py update`.
Please bear in mind that this will overwrite any local custom changes you've made so you should probably back up first.