import json
from datetime import date

def cargar_historial():
    try:
        with open("historial.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    
def guardar_historial(datos):
    with open("historial.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

habitos = {'leer' : 1, 'escribir': 2}

cargar_historial()
guardar_historial(habitos)