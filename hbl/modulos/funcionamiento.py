from cmath import pi
from modulos import hbl as hbl
from modulos import variablesGlobales as VG
from modulos import log as log
from modulos import auxiliar as auxiliar
from modulos.encoderWiegand import Encoder
from modulos import decoderWiegand
from modulos import hblCore as hblCore
import requests

global DNI_data_serial

def Tareas(RunTask):
    global DNI_data_serial
    if RunTask == "Leer Serial":
        if VG.Serial_COM1_Rx_Data != "":
            DNI_data_serial = TareaLeerSerial(VG.Serial_COM1_Rx_Data)
            VG.Serial_COM1_Rx_Data = ""
        if VG.Serial_COM2_Rx_Data != "":
            DNI_data_serial = TareaLeerSerial(VG.Serial_COM2_Rx_Data)         
            VG.Serial_COM2_Rx_Data = ""
    if RunTask == "Enviar Wiegand":
        TareaEnviarWD(DNI_data_serial,pi)
    if RunTask == "Leer Wiegand":
        if VG.WD1_Data != "":
            ID_data_WD = TareaLeerWD(VG.WD1_Data ,1)
            VG.WD1_Data = ""
        if VG.WD2_Data != "":
            ID_data_WD = TareaLeerWD(VG.WD2_Data ,2)
            VG.WD2_Data = ""
    if RunTask == "Request":
        TareaRequest()




def TareaLeerSerial(data):
    log.escribeSeparador(hbl.LOGS_hblTareas)
    log.escribeLineaLog(hbl.LOGS_hblTareas, "Tarea : Leer Serial") 
    log.escribeSeparador(hbl.LOGS_hblTareas)
    log.escribeLineaLog(hbl.LOGS_hblTareas, "Datos Serial recibidos : " + str(data)) 
    VG.NumeroTarea = VG.NumeroTarea+1    ##Esto solo deberia estar cuando se finalice esta tarea
    return str(data)




def TareaEnviarWD(data,pi):
    log.escribeSeparador(hbl.LOGS_hblTareas)
    log.escribeLineaLog(hbl.LOGS_hblTareas, "Tarea : Enviar Wiegand") 

    try:
        ### Extraccion del DNI y envio por Wiegand 34
        valorDNI = auxiliar.splitDNI(data, hbl.LOGS_hblTareas)
        log.escribeLineaLog(hbl.LOGS_hblTareas, "Valor DNI extraido: " + str(valorDNI)) 

        ### Conversion del DNI a wiegand
        DNIWiegand = auxiliar.dniToWiegandConverter(valorDNI, 34, hbl.LOGS_hblTareas)
    except Exception as e:
        print(e)

    if hbl.WD_W1_activado and hbl.WD_W1_modo == "OUT":
        ### Envio codigo wiegand
        try:
            Encoder.encoderWiegandBits(DNIWiegand, pi, VG.Pin_W1_WD0, VG.Pin_W1_WD1) 
            hblCore.encenderLed(pi, 1, int(50))
            log.escribeLineaLog(hbl.LOGS_hblTareas, "Wiegand enviado")
        except Exception as inst:
            print(inst)
    elif hbl.WD_W2_activado and hbl.WD_W2_modo == "OUT":
        try:
            ### Envio codigo wiegand
            Encoder.encoderWiegandBits(DNIWiegand, pi, VG.Pin_W2_WD0, VG.Pin_W2_WD1) 
            hblCore.encenderLed(pi, 1, int(50))
            log.escribeLineaLog(hbl.LOGS_hblTareas, "Wiegand enviado")
        except Exception as inst:
            print(inst)
    else:
        log.escribeSeparador(hbl.LOGS_hblTareas)
        log.escribeLineaLog(hbl.LOGS_hblTareas, "ERROR : Ninugno de los dos WD estan activados y/o en modo salida") 

    VG.NumeroTarea = VG.NumeroTarea + 1




def TareaRequest():
    log.escribeSeparador(hbl.LOGS_hblTareas)
    log.escribeLineaLog(hbl.LOGS_hblTareas, "Tarea : Request") 
    log.escribeSeparador(hbl.LOGS_hblTareas)
    try:
        if hbl.REQ_seleccionURL == 1:
            UrlCompletaReq = hbl.REQ_urlRequest1 + str(id)
        elif hbl.REQ_seleccionURL == 2:
            UrlCompletaReq = hbl.REQ_urlRequest2 + str(id)
        elif hbl.REQ_seleccionURL == 3:
            UrlCompletaReq = hbl.REQ_urlRequest3 + str(id)
        elif hbl.REQ_seleccionURL == 4:
            UrlCompletaReq = hbl.REQ_urlRequest4 + str(id)
        elif hbl.REQ_seleccionURL == 5:
            UrlCompletaReq = hbl.REQ_urlRequest5 + str(id)

        log.escribeLineaLog(hbl.LOGS_hblTareas, "URL Request: " + UrlCompletaReq)

        req = requests.get(UrlCompletaReq, timeout=int(hbl.REQ_timeoutRequest))
        log.escribeLineaLog(hbl.LOGS_hblTareas, "Respuesta Request: " + req)
        VG.NumeroTarea = VG.NumeroTarea + 1

    except Exception as e:
        log.escribeLineaLog(hbl.LOGS_hblTareas, "ERROR Request: ")
        VG.NumeroTarea = VG.NumeroTarea + 1





def TareaLeerWD(id,WD_number):
    flag_data=0
    log.escribeSeparador(hbl.LOGS_hblTareas)
    log.escribeLineaLog(hbl.LOGS_hblTareas, "Tarea : Leer Wiegand") 
    log.escribeSeparador(hbl.LOGS_hblTareas)

    log.escribeLineaLog(hbl.LOGS_hblTareas, "ID WD" + str(WD_number) + " = " + str(id)) 
    VG.NumeroTarea = VG.NumeroTarea + 1
    
    

    




def Control(pi2):
    global pi
    pi = pi2
    if VG.NumeroTarea > hbl.CantidadTareas:
        VG.NumeroTarea = 1

    if VG.NumeroTarea == 1:
        VG.TareaAcutal = hbl.TareasJSON['Tarea1']
        Tareas(hbl.TareasJSON['Tarea1'])
                
    if VG.NumeroTarea == 2:
        VG.TareaAcutal = hbl.TareasJSON['Tarea2']
        Tareas(hbl.TareasJSON['Tarea2'])
        

    if VG.NumeroTarea == 3:
        VG.TareaAcutal = hbl.TareasJSON['Tarea3']
        Tareas(hbl.TareasJSON['Tarea3'])

    if VG.NumeroTarea == 4:
        VG.TareaAcutal = hbl.TareasJSON['Tarea4']
        Tareas(hbl.TareasJSON['Tarea4'])

    if VG.NumeroTarea == 5:
        VG.TareaAcutal = hbl.TareasJSON['Tarea5']
        Tareas(hbl.TareasJSON['Tarea5'])

    if VG.NumeroTarea == 6:
        VG.TareaAcutal = hbl.TareasJSON['Tarea6']
        Tareas(hbl.TareasJSON['Tarea6'])

    if VG.NumeroTarea == 7:
        VG.TareaAcutal = hbl.TareasJSON['Tarea7']
        Tareas(hbl.TareasJSON['Tarea7'])

    if VG.NumeroTarea == 8:
        VG.TareaAcutal = hbl.TareasJSON['Tarea8']
        Tareas(hbl.TareasJSON['Tarea8'])

    if VG.NumeroTarea == 9:
        VG.TareaAcutal = hbl.TareasJSON['Tarea9']
        Tareas(hbl.TareasJSON['Tarea9'])

    if VG.NumeroTarea == 10:
        VG.TareaAcutal = hbl.TareasJSON['Tarea10']
        Tareas(hbl.TareasJSON['Tarea10'])          
    