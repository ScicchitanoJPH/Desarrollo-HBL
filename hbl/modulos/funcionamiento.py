from modulos import hbl as hbl


TareasJSON = hbl.data['Tareas']
CantidadTareas = 0

for key in TareasJSON:
    if TareasJSON[key] != "":
        CantidadTareas = CantidadTareas + 1




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
    
    if NumTask >= CantidadTareas:
        NumTask = 1
    if NumTask == 1:
        return Tareas(TareasJSON['Tarea1'],NumTask)
    if NumTask == 2:
        return Tareas(TareasJSON['Tarea2'],NumTask)
    if NumTask == 3:
        return Tareas(TareasJSON['Tarea3'],NumTask)
    if NumTask == 4:
        return Tareas(TareasJSON['Tarea4'],NumTask)
    if NumTask == 5:
        return Tareas(TareasJSON['Tarea5'],NumTask)
    if NumTask == 6:
        return Tareas(TareasJSON['Tarea6'],NumTask)
    if NumTask == 7:
        return Tareas(TareasJSON['Tarea7'],NumTask)
    if NumTask == 8:
        return Tareas(TareasJSON['Tarea8'],NumTask)
    if NumTask == 9:
        return Tareas(TareasJSON['Tarea9'],NumTask)
    if NumTask == 10:
        return Tareas(TareasJSON['Tarea10'],NumTask)                                
    