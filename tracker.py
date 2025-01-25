### RASTREADOR DE HÁBITOS ###

# --- SECCIÓN: Importación de librerías y módulos ---

from datetime import datetime
from data_manager import guardar_habitos, leer_habitos, comprobar_fecha
import tkinter as tk
from tkinter import messagebox

# --- SECCIÓN: Lógica del Rastreador de Hábitos ---

#Variables
habitos = leer_habitos()

fecha = datetime.now().strftime('%d/%m/%Y')


historial = {
    "fecha" : fecha,
    "habitos" : habitos
}

def mostrar_menu():
    #Menu principal
    print("======== Easy Habit Tracker ========")
    print(f"Hoy es {fecha}")
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
            guardar_habitos(historial) #Al salir guardamos los datos
            break
        else:
            print("---------")
            print("Opcion invalida, intentalo de nuevo")
            print("---------")
            
def anadir_habito():
    valor = habito.get().strip()  # Obtener el valor del input y eliminar espacios extra
    
    if not valor: 
        # Si la cadena está vacía, mostramos un mensaje de error
        messagebox.showerror("Error", "Por favor introduce un hábito válido.")
    elif valor.lower() in habitos:
        # Si el hábito ya existe, mostramos una advertencia
        messagebox.showwarning("Aviso", f"El hábito '{valor}' ya está registrado.")
    else:
        # Si el hábito es válido, lo añadimos
        habitos[valor.lower()] = "Pendiente"
        messagebox.showinfo("Éxito", f"Hábito '{valor}' añadido con éxito.")
        guardar_habitos(historial)
        habito.set("")  # Limpiar el campo de entrada

def actualizar_habito():
    #Funcion para actualizar el estado del habito
    valor = habito.get().strip()

    if valor.lower() == "":
            #Si el usuario no introduce nada, mensaje de error y vuelve a pedir habito
            messagebox.showerror("Error", "Por favor introduce un hábito válido.")
    elif valor.lower() not in habitos:
        messagebox.showerror("Error", f"No estas haciendo seguimiento del hábito {valor.capitalize()}")
    elif habitos[valor.lower()] == "Completado":
            messagebox.showerror("Error", "Ese hábito ya esta marcado como completado")
    else:
        #Si el habito coincide con alguno del diccionario, cambio su valor a "Completado"
        habitos[valor] = "Completado"
        messagebox.showinfo("Éxito", f"Hábito '{valor.capitalize()}' marcado como completado. ¡Bien hecho!")
        guardar_habitos(historial)
        habito.set("")  # Limpiar el campo de entrada

def ver_progreso():
    #Funcion para ver el progreso actual de habitos
    print("-------------")
    count = 0
    if len(historial["habitos"]) == 0:
        #Si no hay habitos registrados mensaje de error
        print("No tienes hábitos registras aún. ¡Añade uno para empezar!")
    else:
        #Imprime el progreso actual
        print("Este es tu progreso de hoy")
        for clave, valor in historial["habitos"].items(): 
            count += 1
            print(f"{count}.  {clave.capitalize()}: {valor}")
    print("-------------")

def eliminar_habito():
    #Funcion para eliminar seguimiento de un habito
    valor = habito.get().strip()
    if valor.lower() in habitos:
        resultado = messagebox.askquestion("Eliminar", f"Estas seguro de querer eliminar el hábito {valor.capitalize()}")
        if resultado == "yes": 
            del habitos[valor.lower()]
            guardar_habitos(historial)
            habito.set("")
    elif valor.lower() == "":
        messagebox.showerror("Error", "No has escrito nada")
    elif valor.lower() not in habitos:
        messagebox.showerror("Error", f"No estas haciendo seguimiento del hábito {valor.capitalize()}")


# --- SECCIÓN: GUI ---
#Ventana Princpal
root = tk.Tk()
root.title("Habit Tracker")
root.geometry("300x300")
root.configure(bg="cyan")
#Variables
habito = tk.StringVar()
#Display
title = tk.Label(root, text=f"HABIT TRACKER\n{fecha}", font=("Arial", 18, "bold"), fg="white", bg="cyan").pack()

#Entrada de texto
entrada = tk.Entry(root, textvariable=habito).pack()

#Botones
boton1 = tk.Button(root, text="Añadir hábito", command=anadir_habito).pack(side="top")
boton2 = tk.Button(root, text="Actualizar hábito", command=actualizar_habito).pack(side="top")
boton3 = tk.Button(root, text="Ver progreso").pack(side="top")
boton4 = tk.Button(root, text="Eliminar hábito", command=eliminar_habito).pack(side="top")
boton5 = tk.Button(root, text="Salir").pack(side="top")

# --- SECCIÓN: Ejecución ---
root.mainloop()


