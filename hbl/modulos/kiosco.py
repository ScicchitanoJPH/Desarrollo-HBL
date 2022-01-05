import os
from modulos import hbl as hbl

def inicializacion():
    #Falta implmentar log de este modulo
    #Implmentar Selenium

    if(hbl.KIOSCO_activado):

        URL = "XAUTHORITY=/root/Xauthority firefox -kiosk -printing -private-window " + "'" + hbl.KIOSCO_URL + "' " + "-width " + hbl.KIOSCO_width + " -height " + hbl.KIOSCO_height + " &"

        print("abriendo firefox")
        os.system("xhost +SI:localuser:root")
        os.system("xset -dpms")
        os.system("xset s off")
        os.system("xset s noblank")
        os.system(URL)
        print(URL)
        print("Listo")