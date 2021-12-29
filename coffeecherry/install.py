#!/bin/python3
import os
import sys

if sys.argv[1]=="install":
    print("Installing...")
    # move app.py to root
    if not os.path.exists("/home/pi/coffeecherry-pi/coffeecherry.py"):
        os.symlink("/home/pi/coffeecherry-pi/coffeecherry/coffeecherry.py","/home/pi/coffeecherry-pi/coffeecherry.py")

    # set-up systemd service
    if not os.path.exists("/home/pi/.config/systemd/user/coffeecherry.service"):
        os.makedirs("/home/pi/.config/systemd/user",exist_ok=True)
        os.symlink("/home/pi/coffeecherry-pi/coffeecherry/coffeecherry.service","/home/pi/.config/systemd/user/coffeecherry.service")
        os.system("systemctl enable --now --user coffeecherry.service")
        os.system("systemctl enable --now --user pigpiod.service")

elif sys.argv[1]=="update":
    print("Updating...")
    os.system("systemctl restart --user coffeecherry.service")
