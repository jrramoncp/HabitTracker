import json
from datetime import date

#Cargar historial
#Actualizar historial
    #Añadir fecha de completado
#Guardar hisotrial
def cargar_historial():
    #CARGAR EL HISTORIAL
    try: 
        with open("historial.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    
def guardar_historial(datos):
    #GUARDAR EL HISTORIAL
    with open("historial.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def actualizar_historial(usuario, habito):
    #ACTUALIZAR EL HISTORIAL
    historial = cargar_historial()
    fecha_actual = date.today().isoformat()

    if usuario not in historial:
        historial [usuario] = {}
    if habito not in historial[usuario]:
        historial[usuario][habito] = []

    historial[usuario][habito].append(fecha_actual)
    guardar_historial(historial)

def imprimir_historial(usuario):
    #IMPRIMIR HISTORIAL
    historial = cargar_historial()
    
    for habito, valor in historial[usuario].items():
        print(f"{habito}, {valor}")

