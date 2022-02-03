#!/usr/bin/env python3

""" --------------------------------------------------------------------------------------------

    _   _ ____  _     
   | | | | __ )| |    
   | |_| |  _ \| |    
   |  _  | |_) | |___ 
   |_| |_|____/|_____|
                   
   (Hardware building layers)
   v1.0

-------------------------------------------------------------------------------------------- """
  
import os
import sys  
import pigpio 
import signal
import time 
import datetime 

import main
from modulos import delays as delays
from modulos import hbl as hbl
from modulos import hidDevice as hidDevice
from modulos import i2cDevice as i2cDevice
from modulos import tcp as tcp
from modulos import log as log
from modulos import hblCore as hblCore 
from modulos import conexiones as conexiones 
from modulos import reporte as reporte 
from modulos import ftp as ftp 
from modulos import tcp as tcp
from modulos import redundancia as redundancia 
from modulos import httpServer as httpServer  
from modulos import serial as serial
from modulos import kiosco as kiosco
from modulos import MQTT as MQTT
from modulos import Monitoreo as Monitoreo

from modulos.decoderWiegand import Decoder
from modulos.encoderWiegand import Encoder
from modulos.salidas import Salidas
from modulos.entradas import Entradas 
from modulos import variablesGlobales as variablesGlobales

global pi


""" --------------------------------------------------------------------------------------------

   signals

-------------------------------------------------------------------------------------------- """
  
def receiveSignal(signalNumber, frame):
   print("Signal received: ", signalNumber) 
   print("Cleaning ...")
   hidDevice.threadCount()
   w.cancel()                         # cancela el callback de wiegand
   pi.stop()                          # detiene el pigpiod
   os.system("sudo killall pigpiod")  # elimina el deamon del pigpiod
   os.system("sudo killall wvdial")   # eliminar proceso del modem  
   sys.exit()                         # sale del hbl
 
""" --------------------------------------------------------------------------------------------

   main

-------------------------------------------------------------------------------------------- """
  
if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
   def callback():
      pass
                                                                                                                                        
   pi = pigpio.pi()

   # cargar parametros del archivo de configuracion
   hbl.cargarParametros('hbl.json') 

   # escribe inicializacion HBL
   hblCore.inicializacionHBL()   

   # inicializa las salidas de la hbl
   main.Salidas(pi)

   # inicializa las entradas de la hbl
   main.Entradas(pi, hbl.DIG_in_in1_pin, hbl.DIG_in_in2_pin, callback)

   # inicializa decoder wiegand
   if hbl.WD_port0_activado == 1:
      w = main.Decoder(pi, hbl.WD_port0_pin_WD0, hbl.WD_port0_pin_WD1, callback)
   
   # inicializa encoder wiegand
   if hbl.WD_port1_activado == 1:
      main.Encoder(pi, hbl.WD_port1_pin_WD0, hbl.WD_port1_pin_WD1)   
 
   # inicializa displays LCD  
   i2cDevice.inicializacion(pi)  
   
   # inicializa dispositivos HID
   hidDevice.inicializacion(pi)     
     
   # inicializa display oled
   hblCore.inicializaoled()

   # inicializa httpServer
   httpServer.inicializacion(pi)

   # signals
   signal.signal(signal.SIGINT, receiveSignal)  
   signal.signal(signal.SIGTERM, receiveSignal)
 
   # configuracion de interfaces de red ETH/WLAN
   conexiones.NetworkConfig() 

   # iniciaizacion GSM Modem ppp0
   conexiones.GSM_Modem_Init()

   # inicia reporte HBL
   reporte.inicializacion()

   # inicio Redundancia HBL
   redundancia.inicializacion()

   # inicializacion modulo serial
   serial.inicializacion(pi)
   
   # Check inicial leds y buzzer
   hblCore.checkLedsBuzzer(pi) 

   # inicializa la comunicacion TCP
   tcp.inicializacion(pi)

   kiosco.inicializacion()

   client = MQTT.inicializacion()


   # heartbeat hblCore
   while True:

      hblCore.heartBeat(pi)
      hblCore.oledRefresh()   
      #MQTT.publish(client)
      MQTT.subscribe(client,pi)
      Monitoreo()



   w.cancel()
   pi.stop() 
