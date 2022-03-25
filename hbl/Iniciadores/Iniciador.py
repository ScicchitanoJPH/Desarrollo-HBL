import os
from colorama import Fore , Style
import time
Folder_Iniciadores_Path  = "/usr/programas/hbl/Iniciadores/"
while 1:
    #print(Fore.GREEN + "1) Salidas \n")
    #print(Fore.RED + "1) Salidas \n")
    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del comando que desea ejecutar:\n")

    print(Fore.LIGHTBLUE_EX + "1) Apagar \n")
    print("2) Reiniciar \n")
    print("3) Actualizar HBL \n")
    print("4) Informacion de CPU \n")
    print("5) Medir Temperatura \n")
    print("6) Mostrar IP \n")
    print("7) Ocultar Aviso Baja Tension \n")
    print("8) Informacion de particiones \n")
    print("9) Informacion de RAM \n")
    print("10) Ver Fecha \n")
    print("11) Informacion de version \n")
    print("12) Ver JSON \n")


         
    Test=int(input())

    print(Fore.LIGHTYELLOW_EX + "\n\n\n")
    if Test==1:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Apagar.sh")
    if Test==2:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Reiniciar.sh")
    if Test==3:
        os.system("sudo sh " + Folder_Iniciadores_Path + "ActualizarHBL.sh")
    if Test==4:
        os.system("sudo sh " + Folder_Iniciadores_Path + "CPU_Info.sh")
    if Test==5:
        os.system("sudo sh " + Folder_Iniciadores_Path + "MedirTemperatura.sh")
    if Test==6:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Mostrar_IP.sh")
    if Test==7:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Ocultar_Aviso_Baja_Tension.sh")
    if Test==8:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Particiones_Info.sh")
    if Test==9:
        os.system("sudo sh " + Folder_Iniciadores_Path + "RAM_Info.sh")
    if Test==10:
        os.system("sudo sh " + Folder_Iniciadores_Path + "VerFecha.sh")
    if Test==11:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Version_Info.sh")  
    if Test==12:
        os.system("sudo sh " + Folder_Iniciadores_Path + "VerJSON.sh")        

    time.sleep(1)
    print("\n\n\n")             
    