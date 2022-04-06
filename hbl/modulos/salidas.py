import pigpio
 
from modulos import hbl as hbl
from modulos import delays as delays
from modulos import auxiliar as auxiliar
from modulos import variablesGlobales as variablesGlobales

""" --------------------------------------------------------------------------------------------

   Clase salidas hbl
   
-------------------------------------------------------------------------------------------- """

class Salidas:

    def __init__(self, pi):
        auxiliar.EscribirFuncion("Salidas - __init__")

        self.pi = pi 

        self.pi.write(Pin_Salida1, hbl.OFF)   
        self.pi.write(Pin_Salida2, hbl.OFF) 
        self.pi.write(Pin_Salida3, hbl.OFF) 
        self.pi.write(Pin_Salida4, hbl.OFF)

        # si el port0 de wiegand esta desactivado, puedo usar los
        # pines como salidas digitales, las inicializo

        if hbl.WD_port0_activado == 0:

            self.pi.write(Pin_Salida5, hbl.OFF)   
            self.pi.write(Pin_Salida6, hbl.OFF) 
            self.pi.write(Pin_Salida7, hbl.OFF) 
            self.pi.write(Pin_Salida8, hbl.OFF)

    def activaSalida(self, pi, pin, tiempo):
        auxiliar.EscribirFuncion("Salidas - activaSalida")
        self.pi.write(Pin_Salida1, hbl.ON) 
        delays.ms(int(tiempo))
        self.pi.write(Pin_Salida1, hbl.OFF)  
    
    def cambioEstadoSalida(self, pi, pin, estado): 
        auxiliar.EscribirFuncion("Salidas - cambioEstadoSalida")
        self.pi.write(pin, estado)
 