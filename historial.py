import json
from datetime import datetime

fecha = datetime.now().strftime('%d/%m/%Y')

#ACTUALIZAR
def guardar_habitos(dic):
    #FUNCION PARA GUARDAR HABITOS EN UN FICHERO JSON, SI NO EXISTE CREA EL FICHERO
    filename = "habitos.json"
    with open (filename, 'w') as archivo:
        json.dump(dic, archivo, indent=4)


#CARGAR HISTORIAL
def leer_habitos():
    filename = "habitos.json"
    try:
        #LEE EL ARCHIVO JSON Y DEVUELVE DICCIONARIO CON LOS DATOS
        with open (filename, 'r') as archivo:
            datos = json.load(archivo)
    
    except FileNotFoundError:
        #SI NO ENCUENTRA EL ARCHIVO, CREA UN ARCHIVO JSON EN BLANCO
        datos = {"fecha" : fecha, "habitos" : {}}

    if datos["fecha"] != fecha:
        for habito in datos["habitos"]:
            datos["habitos"][habito] = "pendiente"
        datos["fecha"] = fecha

    with open (filename, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    return datos["habitos"]
    
#COMPROBAR FECHA Y MODIFICAR A PENDIENTE SI LA FECHA ACTUAL NO ES LA MISMA QUE HAY GUARDADA
def comprobar_fecha():
    filename = "habitos.json"

    with open (filename, "r") as archivo:
        datos = json.load(archivo)

    if datos["fecha"] != fecha:
        for habito in datos["habitos"]:
            datos["habitos"][habito] = "pendiente"

    with open (filename, 'w') as archivo:
        json.dump(datos, archivo, indent=4)



