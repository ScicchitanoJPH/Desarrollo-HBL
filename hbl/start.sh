#!/bin/sh

cd /
cd /usr/programas
sudo git pull origin master
cd /usr/programas/hbl
sudo pigpiod &
sudo python3 main.py &