#!/bin/sh

cd /
sudo cp /usr/programas/hbl/modulos/hbl.json /home/pi/Desktop  ##Hago un backup del hbl.json
cd /usr/programas
sudo git pull origin master ## Actualizo el repositorio si es que hay alguna actualizacion pendiente
sudo python3 CargarParametrosJSON.py  ##Cargo los parametros del JSON original en el nuevo JSON
cd /usr/programas/hbl
sudo pigpiod &
sudo python3 main.py &