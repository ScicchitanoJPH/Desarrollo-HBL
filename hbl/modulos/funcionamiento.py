from cmath import pi
from modulos import hbl as hbl
from modulos import variablesGlobales as VG
from modulos import log as log
from modulos import auxiliar as auxiliar
from modulos.encoderWiegand import Encoder
from modulos import hblCore as hblCore

global DNI_data


def Tareas(RunTask):
    global DNI_data
    if RunTask == "Leer Serial":
        if VG.Serial_COM1_Rx_Data != "":
            DNI_data = TareaLeerSerial(VG.Serial_COM1_Rx_Data)
            VG.Serial_COM1_Rx_Data = ""
        if VG.Serial_COM2_Rx_Data != "":
            DNI_data = TareaLeerSerial(VG.Serial_COM2_Rx_Data)         
            VG.Serial_COM2_Rx_Data = ""
    if RunTask == "Enviar Wiegand":
        TareaEnviarWD(DNI_data,pi)




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


def Control(pi2):
    global pi
    pi = pi2
    if VG.NumeroTarea >= hbl.CantidadTareas:
        VG.NumeroTarea = 1

    if VG.NumeroTarea == 1:
        VG.TareaAcutal = hbl.TareasJSON['Tarea1']
        Tareas(hbl.TareasJSON['Tarea1'])
                
    if VG.NumeroTarea == 2:
        VG.TareaAcutal = hbl.TareasJSON['Tarea2']
        Tareas(hbl.TareasJSON['Tarea2'])
        

    if VG.NumeroTarea == 3:
        VG.TareaAcutal = hbl.TareasJSON['Tarea3']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 4:
        VG.TareaAcutal = hbl.TareasJSON['Tarea4']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 5:
        VG.TareaAcutal = hbl.TareasJSON['Tarea5']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 6:
        VG.TareaAcutal = hbl.TareasJSON['Tarea6']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 7:
        VG.TareaAcutal = hbl.TareasJSON['Tarea7']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 8:
        VG.TareaAcutal = hbl.TareasJSON['Tarea8']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 9:
        VG.TareaAcutal = hbl.TareasJSON['Tarea9']
        VG.NumeroTarea+1

    if VG.NumeroTarea == 10:
        VG.TareaAcutal = hbl.TareasJSON['Tarea10']
        VG.NumeroTarea+1                       
    