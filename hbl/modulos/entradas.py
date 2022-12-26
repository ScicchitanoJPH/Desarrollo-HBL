
import pigpio
import datetime 

from modulos import log as log
from modulos import variablesGlobales as VG
from modulos import hbl as hbl
from modulos import cacheo as cacheo
from modulos import auxiliar as auxiliar
from modulos import Control_Personal as Control_Personal
 
""" --------------------------------------------------------------------------------------------


   Clase entradas hbl


-------------------------------------------------------------------------------------------- """

class Entradas: 

    def __init__(self, pi, in1, in2, in3, in4, callback):
        auxiliar.EscribirFuncion("Entradas - __init__")

        self.pi = pi
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4

        self.callback = callback
 
        self.pi.set_mode(in1, pigpio.INPUT)
        self.pi.set_mode(in2, pigpio.INPUT) 
        self.pi.set_mode(in3, pigpio.INPUT)
        self.pi.set_mode(in4, pigpio.INPUT) 
        
        self.in1 = self.pi.callback(in1, pigpio.FALLING_EDGE, self.callbackIN1)
        self.in2 = self.pi.callback(in2, pigpio.FALLING_EDGE, self.callbackIN2)
        self.in3 = self.pi.callback(in3, pigpio.FALLING_EDGE, self.callbackIN3)
        self.in4 = self.pi.callback(in4, pigpio.FALLING_EDGE, self.callbackIN4)  

    # ***************************************************************************************

    #   callback interrupcion entrada 1 HBL

    # ***************************************************************************************    
    
    def callbackIN1(self, gpio, level, tick): 
        auxiliar.EscribirFuncion("Entradas - callbackIN1")

        diff = pigpio.tickDiff(VG.pressTick, tick)

        log.escribeSeparador(hbl.LOGS_hblEntradas) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "pressTick : " + str(VG.pressTick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff))  

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, hbl.DIG_in_in1_id) 

            VG.Pulso_Anterior_IN1 = 1

            Control_Personal.intruso_detectado()





             
    
    # ***************************************************************************************

    #   callback interrupcion entrada 2 HBL

    # ***************************************************************************************

    def callbackIN2(self, gpio, level, tick):  
        auxiliar.EscribirFuncion("Entradas - callbackIN2")
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        log.escribeSeparador(hbl.LOGS_hblEntradas) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "pressTick : " + str(VG.pressTick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, hbl.DIG_in_in2_id) 
        
            VG.Pulso_Anterior_IN2 = 1

    

    # ***************************************************************************************

    #   callback interrupcion entrada 3 HBL

    # ***************************************************************************************

    def callbackIN3(self, gpio, level, tick):  
        auxiliar.EscribirFuncion("Entradas - callbackIN3")
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        log.escribeSeparador(hbl.LOGS_hblEntradas) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "pressTick : " + str(VG.pressTick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, hbl.DIG_in_in3_id) 
        
            VG.Pulso_Anterior_IN3 = 1

    # ***************************************************************************************

    #   callback interrupcion entrada 4 HBL

    # ***************************************************************************************

    def callbackIN4(self, gpio, level, tick):  
        auxiliar.EscribirFuncion("Entradas - callbackIN4")
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        log.escribeSeparador(hbl.LOGS_hblEntradas) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "pressTick : " + str(VG.pressTick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, hbl.DIG_in_in4_id) 
        
            VG.Pulso_Anterior_IN4 = 1
            
 

    @staticmethod
    def readPin(pi, pin):
        auxiliar.EscribirFuncion("Entradas - readPin")
        
        valorPin = pi.read(pin)
        return valorPin

 