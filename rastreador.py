def mostrar_menu():
    #Menu principal
    print("Bienvenido al Rastreador de Habitos")
    print("1. Añadir un nuevo hábito")
    print("2. Marcar hábito como completado")
    print("3. Ver progreso diario")
    print("4. Salir")

def main():
    #Bucle Principal interfaz CLI
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción: ")
    
        if int(opcion) == 1:
            anadir_habito()
        elif int(opcion) == 2: 
            actualizar_habito()
        elif int(opcion) == 3:
            print("Has elegido ver tu progreso con un hábito (pendiente)")
        elif int(opcion) == 4: 
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida, intentalo de nuevo")
            
habitos = {} #diccionario de habitos, (habito : estado)

def anadir_habito():
    #Funcion para añadir un hábito nuevo
    nombre = input("Introduce tu nuevo hábito: ")
    habitos[nombre] = "Pendiente"
    print("Hábito añadido correctamente")

def actualizar_habito():
    #Funcion para actualizar el estado del habito
    nombre = input("Introduce el hábito que quieres marcar como completado: ")
    if nombre in habitos:
        #Si el nombre coincide con alguno del diccionario, cambio su valor a "Completado"
        habitos[nombre] = "Completado"
        print("Felicidades, has marcado un hábito")
    else:
        #Si el nombre introducio no coincide, imprime mensaje de error
        print("No estas haciendos siguimiento de ese hábito")
        while True:
            nuevo = input("¿Quieres añadirlo como nuevo hábito? Si | No ")
            #Da la posibilidad de añadir un nuevo habito al diccionario
            if nuevo.lower() == "si":
                #Si el usuario indica que si, añade el nuevo habito al diccionario
                habitos[nombre] = "Pendiente"
                break
            if nuevo.lower() == "no":
                print("De acuerdo... volviendo al menú principal")
                break
            else: 
                print("Respuesta no válida, vuelve a intentarlo")






main()
