import json
from datetime import date

#ACTUALIZAR
def guardar_habitos(dic):
    #FUNCION PARA GUARDAR HABITOS EN UN FICHERO JSON, SI NO EXISTE CREA EL FICHERO
    filename = "habitos.json"
    with open (filename, 'w') as archivo:
        json.dump(dic, archivo, indent=4)


#CARGAR HISTORIAL
def leer_historial():
    filename = "habitos.json"
    try:
        #LEE EL ARCHIVO JSON Y DEVUELVE DICCIONARIO CON LOS DATOS
        with open (filename, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        #SI NO ENCUENTRA EL ARCHIVO, CREA UN ARCHIVO JSON EN BLANCO
        with open (filename, 'w') as archivo:
            json.dump({},archivo, indent=4)
            return {}