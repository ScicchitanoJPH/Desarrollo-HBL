import os
from modulos import hbl as hbl

def inicializacion():
    URL = "XAUTHORITY=/root/Xauthority firefox -kiosk -printing -private-window " + "'" + hbl.WD_URL + "' " + "-width 1280 -height 1080 &"

    print("abriendo firefox")
    os.system("xhost +SI:localuser:root")
    os.system("xset -dpms")
    os.system("xset s off")
    os.system("xset s noblank")
    os.system(URL)
    print(URL)
    print("Listo")