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
            

main()