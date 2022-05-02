import os

""" --------------------------------------------------------------------------------------------

   leer los numeros de serie / revision / mac address de la RPI

   ej:

    # MAC Address del Ethernet adapter
    ethtool --show-permaddr eth0    
    # res : dc:a6:32:52:2d:ee

    # otro metodo :
    $ vcgencmd otp_dump | grep '65:' 
    $ vcgencmd otp_dump | grep '64:' 

    # MAC Address del WiFi adapter
    ethtool --show-permaddr wlan0   

    # averiguar el numero de serie de la RPI
    $ vcgencmd otp_dump | grep '28:' 
    # res : 28:f9976413

    # averiguar la revision de la RPI (2G, 4G, etc)
    $ vcgencmd otp_dump | grep '30:' 
    # res : 30:00c03112

-------------------------------------------------------------------------------------------- """

def leer_numero_serie():
    numeroSerie = os.popen("vcgencmd otp_dump | grep '28:'").readline()
    numeroSerie = numeroSerie.replace("\n", "")
    return (numeroSerie.replace("28:", ""))

def leer_revision():
    revision = os.popen("vcgencmd otp_dump | grep '30:'").readline()
    revision = revision.replace("\n", "")
    return (revision.replace("30:", ""))

def leer_MAC_Address(interfase):
    macAddress = os.popen("ethtool --show-permaddr " + interfase).readline()
    macAddress = macAddress.replace("\n", "")
    return (macAddress.replace("Permanent address: ", "")) 

""" ******************************************************************************************

     variables globales  

****************************************************************************************** """ 

#
#   cacheo.py
#

global ubicacionCacheo  
global listaAleatoria
global valorEncontrado 
global cacheoActivo
  

#
#   hblCore.py
#  

global HBLCORE_contadorReset 


#
#   entradas.py
#  
  
global pressTick

#   hidDevice

global jsonEnvioDNI


#   Wiegand
global w1
global w2




# inicializacion variables globales
valorEncontrado = 0
ubicacionCacheo = 0 
cacheoActivo = 0
listaAleatoria = []
HBLCORE_contadorReset = 0
pressTick = 0
jsonEnvioDNI = ""
Seguimiento_file_path = "Seguimiento.txt"

versionHBL = "3.0"

############################################################################
#                                                                          #
#                                 Tareas                                   #
#                                                                          #
############################################################################

TareaAcutal = ""
NumeroTarea = 1
Serial_COM1_Rx_Data = ""
Serial_COM2_Rx_Data = ""


############################################################################
#                                                                          #
#                                Reporte                                   #
#                                                                          #
############################################################################

RPI_SerialNumber = leer_numero_serie()
RPI_Revision = leer_revision()
RPI_MacEthernet = leer_MAC_Address('eth0')
RPI_MacWlan = leer_MAC_Address('wlan0')
NTP_URL = "time.cloudflare.com"

############################################################################
#                                                                          #
#                          Definicion de pines                             #
#                                                                          #
############################################################################

"""       ENTRADAS       """

Pin_Entrada1 = 21
Pin_Entrada2 = 20


"""       SALIDAS       """

Pin_Salida1 = 5
Pin_Salida2 = 6
Pin_Salida3 = 26
Pin_Salida4 = 16

"""     USER LEDS      """

Pin_LED1 = 13
Pin_LED2 = 19
Pin_LED3 = 12
Pin_Buzzer = 18

"""     WIEGAND      """

Pin_W1_WD0 = 23
Pin_W1_WD1 = 24

Pin_W2_WD0 = 17
Pin_W2_WD1 = 27

"""     I2C      """
BusDisplay = 3

