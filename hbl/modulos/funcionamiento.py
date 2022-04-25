from modulos import hbl as hbl

def Tareas(Task,NumTask):
    if Task == "Leer Serial":
        print(Task)
    if Task == "Enviar Wiegand":
        print(Task)
    if Task == "Activar Reles":
        print(Task)
    if Task == "Cacheo":
        print(Task)
    if Task == "Request":
        print(Task)
    if Task == "Recibir Wiegand":
        print(Task)
    
    NumTask = NumTask + 1
    return NumTask



def Control(NumTask):
    
    if NumTask >= hbl.CantidadTareas:
        NumTask = 1
    if NumTask == 1:
        return Tareas(hbl.TareasJSON['Tarea1'],NumTask)
    if NumTask == 2:
        return Tareas(hbl.TareasJSON['Tarea2'],NumTask)
    if NumTask == 3:
        return Tareas(hbl.TareasJSON['Tarea3'],NumTask)
    if NumTask == 4:
        return Tareas(hbl.TareasJSON['Tarea4'],NumTask)
    if NumTask == 5:
        return Tareas(hbl.TareasJSON['Tarea5'],NumTask)
    if NumTask == 6:
        return Tareas(hbl.TareasJSON['Tarea6'],NumTask)
    if NumTask == 7:
        return Tareas(hbl.TareasJSON['Tarea7'],NumTask)
    if NumTask == 8:
        return Tareas(hbl.TareasJSON['Tarea8'],NumTask)
    if NumTask == 9:
        return Tareas(hbl.TareasJSON['Tarea9'],NumTask)
    if NumTask == 10:
        return Tareas(hbl.TareasJSON['Tarea10'],NumTask)                                
    