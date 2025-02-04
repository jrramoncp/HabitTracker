### DESDE AQUÍ MANEJAMOS LA INFORMACIÓN, LECTURA / ESCRITURA DE LOS DATOS EN EL FICHERO JSON"

import json
from datetime import datetime, timedelta

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
    #LEE EL ARCHIVO JSON Y DEVUELVE DICCIONARIO CON LOS DATOS
    try:
        with open (filename, 'r') as archivo:
            datos = json.load(archivo)
    
    #SI NO ENCUENTRA EL ARCHIVO, CREA UN JSON CON UN DICCIONARIO EN BLANCO
    except FileNotFoundError:
        datos = {fecha : {}}
    #SI EL FICHERO JSON ESTA EN BLANCO POR ALGÚN CASUAL
    except json.JSONDecodeError:
        datos = {fecha : {}}
        
    #OBTENER ULTIMA FECHA, PARA CUANDO EMPIEZA UN NUEVO DIA
    if datos:
        ultima_fecha = max(datos.keys(), key=lambda x: datetime.strptime(x, "%d/%m/%Y"))
    else:
        ultima_fecha = None

    #AÑADIR NUEVA KEY AL DICCIONARIO CON LOS VALORES DE LA ULTIMA FECHA REGISTRADA A "PENDIENTE"
    if ultima_fecha:
        habitos_pendientes = {habito: "Pendiente" for habito in datos[ultima_fecha]}
        datos[fecha] = habitos_pendientes

    #GUARDAR DATOS
    with open (filename, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    return datos
    
#COMPROBAR FECHA Y MODIFICAR A PENDIENTE SI LA FECHA ACTUAL NO ES LA MISMA QUE HAY GUARDADA
### EN DESHUSO ACTUALMENTE ###

# def comprobar_fecha():
#     filename = "habitos.json"

#     with open (filename, "r") as archivo:
#         datos = json.load(archivo)

#     if datos["fecha"] != fecha:
#         for habito in datos["habitos"]:
#             datos["habitos"][habito] = "pendiente"

#     with open (filename, 'w') as archivo:
#         json.dump(datos, archivo, indent=4)



