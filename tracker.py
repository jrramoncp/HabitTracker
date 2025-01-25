### RASTREADOR DE HÁBITOS ###

# --- SECCIÓN: Importación de librerías y módulos ---

from datetime import datetime
from data_manager import guardar_habitos, leer_habitos, comprobar_fecha
import tkinter as tk
from tkinter import messagebox

# --- SECCIÓN: Lógica del Rastreador de Hábitos ---

#Variables Principales
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
    count = 0
    if len(historial["habitos"]) == 0:
        #Si no hay habitos registrados mensaje de error
        messagebox.showerror("Error","No tienes hábitos registras aún. ¡Añade uno para empezar!")
    else:
        #Crea una ventana para mostrar el progreso actual
        ventana = tk.Tk()
        ventana.title("Progreso")
        
        ventana.configure(bg="#2C3E50")
        tk.Label(ventana, 
                 text=f"Progreso de hoy {fecha}", 
                 font=("Arial", 16, "bold"), 
                 fg="#ECF0F1", 
                 bg="#2C3E50"
                 ).pack(pady=15, padx=30) 
        for clave, valor in historial["habitos"].items(): 
            count += 1
            tk.Label(ventana, 
                     text=f"{count}.  {clave.capitalize()}: {valor}", 
                     font=("Arial", 12, "bold"), 
                     bg="#2C3E50", 
                     fg="#3498DB").pack(pady=5)

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
root.title("Easy Habit Tracker")
root.geometry("400x350")
root.configure(bg="#2C3E50")
#Variables
habito = tk.StringVar()
#Display
title = tk.Label(root, 
                 text=f"EASY HABIT TRACKER\n{fecha}", 
                 font=("Arial", 18, "bold"), 
                 fg="#3498DB", 
                 bg="#2C3E50"
                 ).pack(padx=30, pady=30)

#Entrada de texto
entrada = tk.Entry(root, 
                   textvariable=habito, 
                   bg="#2C2F33",
                   fg="#FFFFFF", 
                   insertbackground="#7289DA",  
                   highlightthickness=2,
                   highlightbackground="#7289DA",
                   highlightcolor="#99AAB5"
                   ).pack(pady=5)

#Botones
boton1 = tk.Button(root, 
                   text="Añadir hábito", 
                   command=anadir_habito, 
                   bg="#E74C3C", 
                   fg="#ECF0F1",
                   ).pack(pady=5)

boton2 = tk.Button(root, 
                   text="Marcar completado", 
                   command=actualizar_habito, 
                   bg="#E74C3C", 
                   fg="#ECF0F1"
                   ).pack(pady=5)

boton3 = tk.Button(root, 
                   text="Eliminar hábito", 
                   command=eliminar_habito, 
                   bg="#E74C3C", 
                   fg="#ECF0F1").pack(pady=5)

boton4 = tk.Button(root, 
                   text="Ver progreso", 
                   command=ver_progreso, 
                   bg="#E74C3C", 
                   bd=0, 
                   fg="#ECF0F1").pack(pady=5)


boton5 = tk.Button(root, 
                   text="Salir",
                   bg="#2E4053",
                   fg="#FF6F61",
                   command=lambda: root.destroy()
                   ).pack(pady=5)

# --- SECCIÓN: Ejecución ---
root.mainloop()


