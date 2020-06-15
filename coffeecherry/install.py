#!/bin/python3
import pip
import os

# install requirements
with '../requirements' as f:
    package = f.readline()
    pip._internal.main(['install', package])

# move app.py to root
os.symlink('./coffeecherry.py'.'~')

# set-up systemd service
os.symlink('./coffeecherry.service'.'/etc/systemd/system/coffeecherry.service')
os.system('systemctl start coffeecherry.service')
