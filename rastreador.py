def mostrar_menu():
    print("Bienvenido al Rastreador de Habitos")
    print("1. Añadir un nuevo hábito")
    print("2. Marcar hábito como completado")
    print("3. Ver progreso diario")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Introduce una opción: "))
    
        if opcion == 1:
            print("Has elegido un nuevo hábito (pendiente)")
        elif opcion == 2: 
            print("Has elegido marcar un hábito como completado(pendiente)")
        elif opcion == 3:
            print("Has elegido ver tu progreso con un hábito (pendiente)")
        elif opcion == 4: 
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida, intentalo de nuevo")
            
habitos = {}

def añadir_habito():
    nombre = input("Introduce tu nuevo hábito: ")
    habitos[nombre] = "Pendiente"
    print("Hábito añadido correctamente")

def actualizar_habito():
    nombre = input("Introduce el hábito que quieres marcar como completado")
    if nombre in habitos:
        habitos[nombre] = "Completado"
        print("Felicidades, has marcado un hábito")
    else:
        print("No estas haciendos siguimiento de ese hábito")
        nuevo = input("¿Quieres añadirlo como nuevo hábito? Si | No")
        if nuevo.lower() == "si":
            habitos[nombre] = "Pendiente"
        if nuevo.lower() == "no":
            print("De acuerdo... volviendo al menú principal")
        #Bucle para que vuelva al inicio??

añadir_habito()
print(habitos)
print("-----")

actualizar_habito()
print(habitos)

#main()
