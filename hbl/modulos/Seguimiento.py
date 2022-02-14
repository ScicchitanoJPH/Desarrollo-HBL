from modulos import hbl as hbl


def EscribirFuncion(Funcion):
    myFile = open(hbl.Seguimiento_file_path, 'w')
    myFile.write(Funcion)
    myFile.close()