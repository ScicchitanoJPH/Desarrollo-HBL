import os

while 1:
    #print(Fore.GREEN + "1) Salidas \n")
    #print(Fore.RED + "1) Salidas \n")
    print("Ingrese el numero del comando que desea ejecutar:\n")

    print("1) Apagar \n")
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
     
    Test=int(input())
    if Test==1:
        os.system("sudo sh Apagar.sh")
    if Test==2:
        os.system("sudo sh Reiniciar.sh")
    if Test==3:
        os.system("sudo sh ActualizarHBL.sh")
    if Test==4:
        os.system("sudo sh CPU_Info.sh")
    if Test==5:
        os.system("sudo sh MedirTemperatura.sh")
    if Test==6:
        os.system("sudo sh Mostrar_IP.sh")
    if Test==7:
        os.system("sudo sh Ocultar_Aviso_Baja_Tension.sh")
    if Test==8:
        os.system("sudo sh Particiones_Info.sh")
    if Test==9:
        os.system("sudo sh RAM_Info.sh")
    if Test==10:
        os.system("sudo sh VerFecha.sh")
    if Test==11:
        os.system("sudo sh Version_Info.sh")                     
    