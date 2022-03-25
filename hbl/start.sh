#!/bin/sh
if [ $(jq .ActualizarGit.Activado /usr/programas/hbl/modulos/hbl.json) -eq 1 ]; then    #Chequeo en el json si esta activada la actualizacion Git
    echo "----------- Buscando Actualizaciones Git -----------"
    cd /
    sudo cp /usr/programas/hbl/modulos/hbl.json /home/pi/Desktop  ##Hago un backup del hbl.json
    cd /usr/programas
    sudo git reset --hard   #Esto elimina cualquier cambio local que se haya hecho
    sudo git pull origin master ## Actualizo el repositorio si es que hay alguna actualizacion pendiente
    sleep 0.5   #Este sleep es para que termine de actualizar el repo
    cd /
    cd /usr/programas   #Hay que volver a ingresar al path porque cuando se actualiza el repo, el path /usr/programas ya no existe mas
    sudo python3 /usr/programas/hbl/CargarParametrosJSON.py & ##Cargo los parametros del JSON original en el nuevo JSON
fi
cd /usr/programas/hbl
sudo pigpiod &
sudo python3 main.py &