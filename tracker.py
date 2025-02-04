### RASTREADOR DE HÁBITOS ###

# --- SECCIÓN: Importación de librerías y módulos ---

from datetime import datetime
from data_manager import guardar_habitos, leer_habitos, fecha
import tkinter as tk
from tkinter import messagebox

# --- SECCIÓN: Lógica del Rastreador de Hábitos ---

#Variables Principales
#fecha = datetime.now().strftime('%d/%m/%Y')
historial = leer_habitos()

def anadir_habito():
    #Funcion para añadir un hábito nuevo, utiliza la entrada de texto, para añadir una nueva clave a nuestro diccionario, que por defecto, tendra el valor "Pendiente"

    valor = habito.get().strip()  # Obtener el valor del input y eliminar espacios extra
    
    if not valor: 
        # Si la cadena está vacía, mostramos un mensaje de error
        messagebox.showerror("Error", "Por favor introduce un hábito válido.")

    elif valor.lower() in historial:
        # Si el hábito ya existe, mostramos una advertencia
        messagebox.showwarning("Aviso", f"El hábito '{valor}' ya está registrado.")

    else:
        # Si el hábito es válido, lo añadimos
        historial[fecha][valor.lower()] = "Pendiente"
        messagebox.showinfo("Éxito", f"Hábito '{valor}' añadido con éxito.")
        guardar_habitos(historial)
        habito.set("")  # Limpiar el campo de entrada

def actualizar_habito():
    #Funcion para marcar un hábito como completado, utiliza lo que haya escrito el usuario en la entrada de texto para buscar su clave correspondiente en nuestro diccionario y cambiar su valor

    valor = habito.get().strip()

    if valor.lower() == "":
        #Si el usuario no introduce nada, devuelve mensaje de error
        messagebox.showerror("Error", "Por favor introduce un hábito válido.")

    elif valor.lower() not in historial[fecha]:
        #Si el hábito escrito no existe en nuestro diccionario, devuelve mensaje de error
        messagebox.showerror("Error", f"No estas haciendo seguimiento del hábito {valor.capitalize()}")

    elif historial[fecha][valor.lower()] == "Completado":
            #Si el hábito escrito ya tiene el valor "Completado" en nuestro diccionario, devuelve un mensaje de error
            messagebox.showerror("Error", "Ese hábito ya esta marcado como completado")

    else:
        #Si el habito coincide con alguno del diccionario, cambio su valor a "Completado"
        historial[fecha][valor.lower()] = "Completado"
        #Mensaje de confirmación de que se ha realizado la accion
        messagebox.showinfo("Éxito", f"Hábito '{valor.capitalize()}' marcado como completado. ¡Bien hecho!") 
        guardar_habitos(historial) #Actualizamos el historial con el diccionario nuevo
        habito.set("")  # Limpiar el campo de entrada

def ver_progreso():
    #Funcion para ver el progreso actual de habitos
    count = 0 # Este contador nos sirve para más adelante numerar los hábitos dentro de la ventana nueva

    if len(historial[fecha]) == 0:
        #Si no hay habitos registrados muestra mensaje de error
        messagebox.showerror("Error","No tienes hábitos registras aún. ¡Añade uno para empezar!")

    else:
        #Crea una ventana nueva para mostrar el progreso actual
        ventana = tk.Tk()
        ventana.title("Progreso")
        
        ventana.configure(bg="#2C3E50")
        tk.Label(ventana, 
                 text=f"Progreso de hoy {fecha}", 
                 font=("Arial", 16, "bold"), 
                 fg="#ECF0F1", 
                 bg="#2C3E50"
                 ).pack(pady=15, padx=30) 
        
        # Por cada clave (habito) del diccionario, creamos una Label que muestra además el valor (estado)
        for clave, valor in historial[fecha].items(): 
            count += 1
            tk.Label(ventana, 
                     text=f"{count}.  {clave.capitalize()}: {valor}", 
                     font=("Arial", 12, "bold"), 
                     bg="#2C3E50", 
                     fg="#3498DB").pack(pady=5)

def eliminar_habito():
#Funcion para eliminar un hábito del diccionario y así no hacerle seguimiento

    valor = habito.get().strip()

    if valor.lower() in historial[fecha]:
        resultado = messagebox.askquestion("Eliminar", f"Estas seguro de querer eliminar el hábito {valor.capitalize()}")
        if resultado == "yes": 
            del historial[fecha][valor.lower()]
            messagebox.showinfo("Delete", f"Habito {valor.capitalize()} eliminado del registro")
            guardar_habitos(historial)
            habito.set("")
    elif valor.lower() == "":
        messagebox.showerror("Error", "No has escrito nada")
    elif valor.lower() not in historial[fecha]:
        messagebox.showerror("Error", f"No estas haciendo seguimiento del hábito {valor.capitalize()}")

# === SECCIÓN: GUI ===

##Ventana Princpal
# - Ventana principal de la app, donde están alojados el titulo, la entrada de texto y los botones -
root = tk.Tk()
root.title("Easy Habit Tracker")
root.geometry("400x350")
root.configure(bg="#2C3E50")

##Variables de la GUI
# -Esta variable, está mapeada al entry de más adelante, y es lo que la enlaza con las funciones -
habito = tk.StringVar()

##Encabezado
# - Encabezado donde se muestra la fecha y el nombre de la app -
title = tk.Label(root, 
                 text=f"EASY HABIT TRACKER\n{fecha}", 
                 font=("Arial", 18, "bold"), 
                 fg="#3498DB", 
                 bg="#2C3E50"
                 ).pack(padx=30, pady=30)

##Entrada de texto
# -- En esta entrada el usuario escribirá, y servira de enlace con los botones para llevar a cabo las diferentes funciones -- 

entrada = tk.Entry(root, 
                   textvariable=habito, 
                   bg="#2C2F33",
                   fg="#FFFFFF", 
                   insertbackground="#7289DA",  
                   highlightthickness=2,
                   highlightbackground="#7289DA",
                   highlightcolor="#99AAB5"
                   ).pack(pady=5)

##Botones

#Boton añadir hábito
boton_anadir = tk.Button(root, 
                   text="Añadir hábito", 
                   command=anadir_habito, 
                   bg="#E74C3C", 
                   fg="#ECF0F1",
                   ).pack(pady=5)

#Boton para marcar completado
boton_completado = tk.Button(root, 
                   text="Marcar completado", 
                   command=actualizar_habito, 
                   bg="#E74C3C", 
                   fg="#ECF0F1"
                   ).pack(pady=5)

#Boton para eliminar
boton_eliminar = tk.Button(root, 
                   text="Eliminar hábito", 
                   command=eliminar_habito, 
                   bg="#E74C3C", 
                   fg="#ECF0F1").pack(pady=5)

#Boton para ver progreso
boton_progreso = tk.Button(root, 
                   text="Ver progreso", 
                   command=ver_progreso, 
                   bg="#E74C3C", 
                   bd=0, 
                   fg="#ECF0F1").pack(pady=5)


#Boton para salir
boton_salir = tk.Button(root, 
                   text="Salir",
                   bg="#2E4053",
                   fg="#FF6F61",
                   command=lambda: root.destroy()
                   ).pack(pady=5)

# --- SECCIÓN: Ejecución ---
root.mainloop()


