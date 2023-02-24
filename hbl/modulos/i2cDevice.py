import pigpio
 
from modulos import lcd_i2c as lcd_i2c
from modulos import hbl as hbl
from modulos import delays as delays
from modulos import log as log
from modulos import auxiliar as auxiliar
from modulos import variablesGlobales as variablesGlobales


global lcd1
global lcd2
global lcd3
global lcd4

def inicializacion(pi):
    auxiliar.EscribirFuncion("inicializacion")

    global lcd1
    global lcd2
    global lcd3
    global lcd4

    # inicializa displays LCD   
    try:
        if hbl.DISPLAY_activado == 1:
            lcd1 = lcd_i2c.lcd(pi, width=20, bus=variablesGlobales.BusDisplay) 
            delays.ms(100)
            lcd1.put_line(0, "HBL") 
 
    except Exception as inst: 

        log.escribeSeparador(hbl.LOGS_hbli2c) 
        log.escribeLineaLog(hbl.LOGS_hbli2c, "Error : " + str(inst))
    
    
