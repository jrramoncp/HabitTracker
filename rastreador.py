from datetime import datetime
from historial import guardar_habito, leer_historial

def mostrar_menu():
    #Menu principal
    print("======== Easy Habit Tracker ========")
    print(f"Hoy es {datetime.now().strftime('%d/%m/%Y')}")
    print("---------")
    print("1. Añadir un nuevo hábito\n")
    print("2. Marcar hábito como completado\n")
    print("3. Ver progreso diario\n")
    print("4. Eliminar hábito\n")
    print("5. Salir")
    print("---------")

def main():
    #Bucle Principal interfaz CLI
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción: ")
    
        if opcion == "1":
            anadir_habito()
        elif opcion == "2": 
            actualizar_habito()
        elif opcion == "3":
            ver_progreso()
        elif opcion == "4": 
            eliminar_habito()
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("---------")
            print("Opcion invalida, intentalo de nuevo")
            print("---------")
            
habitos = leer_historial() #diccionario de habitos, (habito : estado)

def anadir_habito():
    #Funcion para añadir un hábito nuevo
    print("---------")
    nombre = input("Introduce tu nuevo hábito: ")
    if nombre.lower() in habitos: 
        #Si ya estamos haciendo seguimiento de ese hábito
        print("---------")
        print("Ya estas haciendo seguimiento de ese hábito.")
        print("---------")
    else: 
        #Si no, lo añadimos al diccionario
        habitos[nombre.lower()] = "Pendiente"
        print("---------")
        print(f"Hábito {nombre.capitalize()} añadido correctamente y marcado como 'Pendiente'")
        print("---------")
        guardar_habito(habitos)

def actualizar_habito():
    #Funcion para actualizar el estado del habito
    print("---------")
    nombre = input("Introduce el hábito que quieres marcar como completado: ")
    if nombre.lower() in habitos:
        #Si el nombre coincide con alguno del diccionario, cambio su valor a "Completado"
        habitos[nombre] = "Completado"
        print("---------")
        print(f"{nombre.capitalize()} marcado como completado. ¡Sigue así!")
        print("---------")
    else:
        #Si el nombre introducio no coincide, imprime mensaje de error
        print("---------")
        print("No estas haciendos siguimiento de ese hábito")
        print("---------")
        while True:
            nuevo = input("¿Quieres añadirlo como nuevo hábito? Si | No ")
            #Da la posibilidad de añadir un nuevo habito al diccionario
            if nuevo.lower() == "si":
                #Si el usuario indica que si, añade el nuevo habito al diccionario
                habitos[nombre] = "Pendiente"
                print(f"Habito {nombre} añadido y marcado como 'Pendiente'")
                break
            if nuevo.lower() == "no":
                print("De acuerdo... volviendo al menú principal")
                #Si el usuario indica que no, salimos al menu principal
                break
            else: 
                print("Respuesta no válida, vuelve a intentarlo")
                #Nos aseguramos que la respuesta sea válida

def ver_progreso():
    #Funcion para ver el progreso actual de habitos
    print("-------------")
    count = 0
    if len(habitos) == 0:
        #Si no hay habitos registrados mensaje de error
        print("No tienes hábitos registras aún. ¡Añade uno para empezar!")
    else:
        #Imprime el progreso actual
        print("Este es tu progreso de hoy")
        for clave, valor in habitos.items(): 
            count += 1
            print(f"{count}.  {clave.capitalize()}: {valor}")
    print("-------------")

def eliminar_habito():
    #Funcion para eliminar seguimiento de un habito
    print("---------")
    nombre = input("Introduce el nombre del hábito que quieres eliminar ")
    if nombre.lower() in habitos: 
        while True:
            print("---------")
            print("Atención perderas tu progreso y esta opción es irreversible") #Advertencia
            confirmacion = input("Vuelve a introducir el hábito para confirmar o cancelar para volver al menú principal ") #Confirmacion de que se quiere eliminar el hábito
            if confirmacion.lower() == nombre.lower():
                #Elimina habito y vuelve a inicio
                del habitos[nombre.lower()]
                print("---------")
                print(f"Habito {nombre.capitalize()} eliminado")
                print("---------")
                break
            if confirmacion.lower() == "cancelar":
                #Vuelve a inicio
                break
            else: 
                #Si no es ninguna de las dos opciones, mensaje de error
                print("---------")
                print("Respuesta no válida, vuelve a intentarlo")
                print("---------")
    else: 
        print("---------")
        print("ERROR! No estas haciendo seguimiento de ese hábito")
        print("---------")
        



main()
