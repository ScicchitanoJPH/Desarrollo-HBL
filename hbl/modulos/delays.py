import time
from modulos import Seguimiento as Seguimiento

def ms(tiempo):
    Seguimiento.EscribirFuncion("ms")
    time.sleep(tiempo/1000)