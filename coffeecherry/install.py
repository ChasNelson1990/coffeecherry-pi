#!/bin/python3
import pip
import shutil
import os

# install requirements
with '../requirements' as f:
    package = f.readline()
    pip._internal.main(['install', package])

# move app.py to root
shutil.move('./coffeecherry.py'.'~')

# set-up systemd service
shutil.move('./coffeecherry.service'.'/etc/systemd/system/coffeecherry.service')
os.system('systemctl start coffeecherry.service')
