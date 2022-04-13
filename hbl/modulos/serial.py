
import sys
import os
import serial
import threading
import time
from modulos import auxiliar as auxiliar

from time import sleep 
from serial import SerialException

from modulos import hbl as hbl 
from modulos import log as log
from modulos.encoderWiegand import Encoder
from modulos import hblCore as hblCore
from modulos import variablesGlobales as variablesGlobales
from modulos import auxiliar as auxiliar

global pi
 

""" --------------------------------------------------------------------------------------------

    Thread para la comunicacion serial

-------------------------------------------------------------------------------------------- """

def startThreadSerial(): 
    auxiliar.EscribirFuncion("startThreadSerial")

    global pi

    ser1 = serial.Serial(port=hbl.SERIAL_COM1_port, baudrate=hbl.SERIAL_COM1_baudrate, bytesize=hbl.SERIAL_COM1_bytesize, parity=hbl.SERIAL_COM1_parity, stopbits=hbl.SERIAL_COM1_stopbits)
    ser1.flushInput()

    ser2 = serial.Serial(port=hbl.SERIAL_COM2_port, baudrate=hbl.SERIAL_COM2_baudrate, bytesize=hbl.SERIAL_COM2_bytesize, parity=hbl.SERIAL_COM2_parity, stopbits=hbl.SERIAL_COM2_stopbits)
    ser2.flushInput()
              
    while True: 

        if hbl.FUNC_modo == 8:

            try: 
                received_data = ser1.readline()
                received_data = ser2.readline()
                time.sleep(0.03)
                data_left = ser1.inWaiting()
                data_left = ser2.inWaiting()
                received_data +=ser1.read(data_left) 
                data_left = ser2.inWaiting()

                log.escribeSeparador(hbl.LOGS_hblSerial)
                log.escribeLineaLog(hbl.LOGS_hblSerial, "Datos Serial recibidos : " + str(received_data)) 

                ### Extraccion del DNI y envio por Wiegand 34
                valorDNI = auxiliar.splitDNI(str(received_data), hbl.LOGS_hblSerial)
                log.escribeLineaLog(hbl.LOGS_hblSerial, "Valor DNI extraido: " + str(valorDNI)) 

                ### Conversion del DNI a wiegand
                DNIWiegand = auxiliar.dniToWiegandConverter(valorDNI, 34, hbl.LOGS_hblSerial)
    
                ### Envio codigo wiegand
                Encoder.encoderWiegandBits(DNIWiegand, pi, variablesGlobales.Pin_W2_WD0, variablesGlobales.Pin_W2_WD1) 

                ### Enciende led indicador
                hblCore.encenderLed(pi, 1, int(50))

                log.escribeLineaLog(hbl.LOGS_hblSerial, "Wiegand enviado")  
 
            except Exception as e:
              
                exc_type, exc_obj, exc_tb = sys.exc_info() 
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1] 
                errorExcepcion = "ERROR : " + str(fname) + " - linea : " + str(sys.exc_info()[-1].tb_lineno) + " - mensaje : " + str(exc_obj) 

                log.escribeSeparador(hbl.LOGS_hblSerial)
                log.escribeLineaLog(hbl.LOGS_hblSerial, "Error : " + str(errorExcepcion)) 
        
        time.sleep(0.01)
    
""" --------------------------------------------------------------------------------------------

    inicializacion comunicacion Serial

-------------------------------------------------------------------------------------------- """

def inicializacion(pi2): 
    auxiliar.EscribirFuncion("inicializacion")

    global pi
 
    pi = pi2

    if hbl.SERIAL_COM1_activado == 1:
 
        try:

            serialHBL = threading.Thread(target=startThreadSerial, name='HBLSerial')
            serialHBL.setDaemon(True)
            serialHBL.start()   

            log.escribeSeparador(hbl.LOGS_hblSerial)
            log.escribeLineaLog(hbl.LOGS_hblSerial, "Serial Start")  
        
        except Exception as e:
              
            exc_type, exc_obj, exc_tb = sys.exc_info() 
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1] 
            errorExcepcion = "ERROR : " + str(fname) + " - linea : " + str(sys.exc_info()[-1].tb_lineno) + " - mensaje : " + str(exc_obj) 

            log.escribeSeparador(hbl.LOGS_hblSerial)
            log.escribeLineaLog(hbl.LOGS_hblSerial, "Error : " + str(errorExcepcion)) 

    if hbl.SERIAL_COM2_activado == 1:
 
        try:

            serialHBL = threading.Thread(target=startThreadSerial, name='HBLSerial')
            serialHBL.setDaemon(True)
            serialHBL.start()   

            log.escribeSeparador(hbl.LOGS_hblSerial)
            log.escribeLineaLog(hbl.LOGS_hblSerial, "Serial Start")  
        
        except Exception as e:
              
            exc_type, exc_obj, exc_tb = sys.exc_info() 
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1] 
            errorExcepcion = "ERROR : " + str(fname) + " - linea : " + str(sys.exc_info()[-1].tb_lineno) + " - mensaje : " + str(exc_obj) 

            log.escribeSeparador(hbl.LOGS_hblSerial)
            log.escribeLineaLog(hbl.LOGS_hblSerial, "Error : " + str(errorExcepcion))        