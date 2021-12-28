import pigpio
 
from modulos import hbl as hbl
from modulos import delays as delays

""" --------------------------------------------------------------------------------------------

   Clase salidas hbl
   
-------------------------------------------------------------------------------------------- """

class Salidas:

    def __init__(self, pi):

        self.pi = pi 

        self.pi.write(hbl.DIG_out_pin_out1, hbl.OFF)   
        self.pi.write(hbl.DIG_out_pin_out2, hbl.OFF) 
        self.pi.write(hbl.DIG_out_pin_out3, hbl.OFF) 
        self.pi.write(hbl.DIG_out_pin_out4, hbl.OFF)

        # si el port0 de wiegand esta desactivado, puedo usar los
        # pines como salidas digitales, las inicializo

        if hbl.WD_port0_activado == 0:

            self.pi.write(hbl.DIG_out_pin_out5, hbl.OFF)   
            self.pi.write(hbl.DIG_out_pin_out6, hbl.OFF) 
            self.pi.write(hbl.DIG_out_pin_out7, hbl.OFF) 
            self.pi.write(hbl.DIG_out_pin_out8, hbl.OFF)

    def activaSalida(self, pi, pin, tiempo):
        self.pi.write(hbl.DIG_out_pin_out1, hbl.ON) 
        delays.ms(int(tiempo))
        self.pi.write(hbl.DIG_out_pin_out1, hbl.OFF)  
    
    def cambioEstadoSalida(self, pi, pin, estado): 
        self.pi.write(pin, estado)
 