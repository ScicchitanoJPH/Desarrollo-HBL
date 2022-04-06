
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




# inicializacion variables globales
valorEncontrado = 0
ubicacionCacheo = 0 
cacheoActivo = 0
listaAleatoria = []
HBLCORE_contadorReset = 0
pressTick = 0
jsonEnvioDNI = ""


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
Pin_Salida5 = 27
Pin_Salida6 = 17
Pin_Salida7 = 24
Pin_Salida8 = 23

"""     USER LEDS      """

Pin_LED1 = 13
Pin_LED2 = 19
Pin_LED3 = 12
Pin_Buzzer = 18

"""     WIEGAND      """

Pin_Port1_WD0 = 23
Pin_Port1_WD1 = 19

Pin_Port2_WD0 = 17
Pin_Port2_WD1 = 27


