import datetime
from modulos import SendMail as SendMail
from modulos import auxiliar as auxiliar

file_path = '/usr/programas/hbl/Intrusos_Pendientes.txt'

def add_intruso(date):
    myFile = open(file_path, 'a')

    with myFile:
        myFile.write(date + "\n")
        myFile.close() 

def intruso_detectado():
    if auxiliar.CheckInternet():
        SendMail.send(str(datetime.datetime.now()))
    else:
        add_intruso(str(datetime.datetime.now()))