import json
from datetime import date

historial = {}
#CREAR / GUARDAR HABITOS
def guardar_habito(dic):
    #FUNCION PARA GUARDAR HABITOS EN UN FICHERO JSON, SI NO EXISTE CREA EL FICHERO
    filename = "habitos.json"
    with open (filename, 'w') as habitos:
        json.dump(dic, habitos)

#LEER HISTORIAL
def leer_historial():
    filename = "habitos.json"
    try:
        with open (filename, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        pass
#ACTUALIZAR HISTORIAL
#MOSTRAR HISTORIAL


historial = leer_historial()
print(historial)
