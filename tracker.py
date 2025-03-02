### RASTREADOR DE HÁBITOS ###

# --- SECCIÓN: Importación de librerías y módulos ---

from datetime import datetime
from data_manager import guardar_habitos, leer_habitos, fecha
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

# --- SECCIÓN: Lógica del Rastreador de Hábitos ---

#Variables Principales
#fecha = datetime.now().strftime('%d/%m/%Y')
historial = leer_habitos()
ventana_historial = None #Variable para la funcion historial
ventana_progreso = None #Variable para la funcion progreso
ventana_seleccion = None #Variable para la ventana de selección

def anadir_habito():
    global ventana_historial, ventana_progreso
    #Funcion para añadir un hábito nuevo, utiliza la entrada de texto, para añadir una nueva clave a nuestro diccionario, que por defecto, tendra el valor "Pendiente"

    valor = habito.get().strip()  # Obtener el valor del input y eliminar espacios extra
    
    if not valor: 
        # Si la cadena está vacía, mostramos un mensaje de error
        messagebox.showerror("Error", "Por favor introduce un hábito válido.")

    elif valor.lower() in historial[fecha]:
        # Si el hábito ya existe, mostramos una advertencia
        messagebox.showwarning("Aviso", f"El hábito '{valor}' ya está registrado.")

    else:
        # Si el hábito es válido, lo añadimos
        historial[fecha][valor.lower()] = "Pendiente"
        messagebox.showinfo("Éxito", f"Hábito '{valor}' añadido con éxito.")
        guardar_habitos(historial)
        habito.set("")  # Limpiar el campo de entrada

        # Close the historial window if it is open
        if ventana_historial is not None:
            ventana_historial.destroy()
            ventana_historial = None

        # Close the progreso window if it is open
        if ventana_progreso is not None:
            ventana_progreso.destroy()
            ventana_progreso = None

        # Reopen the progreso window
        ver_progreso()

def actualizar_habito():
    global ventana_historial, ventana_progreso, ventana_seleccion
    #Funcion para marcar un hábito como completado, utiliza lo que haya escrito el usuario en la entrada de texto para buscar su clave correspondiente en nuestro diccionario y cambiar su valor

    def seleccionar_habito():
        global ventana_historial, ventana_progreso, ventana_seleccion
        valor = lista_habitos.get(tk.ACTIVE).strip()

        if valor.lower() == "":
            #Si el usuario no introduce nada, devuelve mensaje de error
            messagebox.showerror("Error", "Por favor selecciona un hábito válido.")

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

            # Close the seleccion window
            ventana_seleccion.destroy()
            ventana_seleccion = None

            # Close the historial window if it is open
            if ventana_historial is not None:
                ventana_historial.destroy()
                ventana_historial = None

            # Close the progreso window if it is open
            if ventana_progreso is not None:
                ventana_progreso.destroy()
                ventana_progreso = None

            # Reopen the progreso window
            ver_progreso()

    # VENTANA PARA SELECCIONAR HABITO
    ventana_seleccion = tk.Toplevel()
    ventana_seleccion.title("Seleccionar Hábito")
    ventana_seleccion.geometry("400x400")
    ventana_seleccion.configure(bg="#2C3E50")

    # LABEL PRINCIPAL TITULO
    tk.Label(ventana_seleccion, 
            text=f"Seleccionar Hábito", 
            font=("Arial", 16, "bold"), 
            fg="#ECF0F1", 
            bg="#2C3E50"
            ).pack(pady=15, padx=30) 

    # LISTBOX PARA MOSTRAR HABITOS
    lista_habitos = tk.Listbox(ventana_seleccion, bg="#2C3E50", fg="#ECF0F1", font=("Arial", 12))
    lista_habitos.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

    for habito in historial[fecha]:
        lista_habitos.insert(tk.END, habito.capitalize())

    # BOTON PARA SELECCIONAR HABITO
    tk.Button(ventana_seleccion, 
              text="Completar", 
              command=seleccionar_habito, 
              bg="#E74C3C", 
              fg="#ECF0F1").pack(pady=10)

def eliminar_habito():
    global ventana_historial, ventana_progreso, ventana_seleccion
    #Funcion para eliminar un hábito del diccionario y así no hacerle seguimiento

    def seleccionar_habito():
        global ventana_historial, ventana_progreso, ventana_seleccion
        valor = lista_habitos.get(tk.ACTIVE).strip()

        if valor.lower() in historial[fecha]:
            resultado = messagebox.askquestion("Eliminar", f"¿Estas seguro de querer eliminar el hábito {valor.capitalize()}")
            if resultado == "yes": 
                del historial[fecha][valor.lower()]
                messagebox.showinfo("Delete", f"Habito {valor.capitalize()} eliminado del registro")
                guardar_habitos(historial)

                # Close the seleccion window
                ventana_seleccion.destroy()
                ventana_seleccion = None

                # Close the historial window if it is open
                if ventana_historial is not None:
                    ventana_historial.destroy()
                    ventana_historial = None

                # Close the progreso window if it is open
                if ventana_progreso is not None:
                    ventana_progreso.destroy()
                    ventana_progreso = None

                # Reopen the progreso window
                ver_progreso()
        elif valor.lower() == "":
            messagebox.showerror("Error", "Por favor selecciona un hábito válido.")
        elif valor.lower() not in historial[fecha]:
            messagebox.showerror("Error", f"No estas haciendo seguimiento del hábito {valor.capitalize()}")

    # VENTANA PARA SELECCIONAR HABITO
    ventana_seleccion = tk.Toplevel()
    ventana_seleccion.title("Seleccionar Hábito")
    ventana_seleccion.geometry("400x400")
    ventana_seleccion.configure(bg="#2C3E50")

    # LABEL PRINCIPAL TITULO
    tk.Label(ventana_seleccion, 
            text=f"Seleccionar Hábito", 
            font=("Arial", 16, "bold"), 
            fg="#ECF0F1", 
            bg="#2C3E50"
            ).pack(pady=15, padx=30) 

    # LISTBOX PARA MOSTRAR HABITOS
    lista_habitos = tk.Listbox(ventana_seleccion, bg="#2C3E50", fg="#ECF0F1", font=("Arial", 12))
    lista_habitos.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

    for habito in historial[fecha]:
        lista_habitos.insert(tk.END, habito.capitalize())

    # BOTON PARA SELECCIONAR HABITO
    tk.Button(ventana_seleccion, 
              text="Eliminar", 
              command=seleccionar_habito, 
              bg="#E74C3C", 
              fg="#ECF0F1").pack(pady=10)

def ver_historial():
    global ventana_historial
    #Funcion para ver los hábitos registrados un día anterior
    
    # VENTANA PARA HISTORIAL
    ventana = tk.Toplevel()
    ventana.title("Historial")
    ventana.geometry("400x400")
    ventana.configure(bg="#2C3E50")

    # LABEL PRINCIPAL TITULO
    tk.Label(ventana, 
            text=f"Historial", 
            font=("Arial", 16, "bold"), 
            fg="#ECF0F1", 
            bg="#2C3E50"
            ).pack(pady=15, padx=30) 
    
    # LABEL MESSAGE
    tk.Label(ventana,
            text="Selecciona una fecha",
            font=("Arial", 12, "bold"),
            fg="#ECF0F1", 
            bg="#2C3E50"
            ).pack(padx=30)
    
    # CALENDARIO
    cal = Calendar(ventana, selectmode="day")
    cal.pack(pady=20, padx=10)

    
    def show_date():
        global ventana_historial

        raw_date = cal.get_date() #Fecha seleccionada sin formatear
         
        date_obj = datetime.strptime(raw_date, "%d/%m/%y") #Convertimos la fecha sin formatear en un objeto

        date = date_obj.strftime("%d/%m/%Y") #Formateamos fecha para poder filtrar en nuestro diccionario
        
        count = 0 #Contador para cuando abramos la ventana con el progreso del día

        try:
            #Si la fecha no existe en nuestro diccionario, la eliminamos
            if date not in historial:
                raise KeyError
            
            # Si ya hay una ventana historial abierta la cerramos para abrir la nueva
            if ventana_historial is not None:
                ventana_historial.destroy()
            
            #Crea una ventana nueva para mostrar ese día
            ventana_historial = tk.Toplevel()
            ventana_historial.title(date)
            
            ventana_historial.configure(bg="#2C3E50")
            tk.Label(ventana_historial, 
                    text=f"Progreso del dia {date}", 
                    font=("Arial", 16, "bold"), 
                    fg="#ECF0F1", 
                    bg="#2C3E50"
                    ).pack(pady=15, padx=30) 
            
            # Por cada clave (habito) del diccionario, creamos una Label que muestra además el valor (estado)
            for clave, valor in historial[date].items(): 
                count += 1
                tk.Label(ventana_historial, 
                        text=f"{count}.  {clave.capitalize()}: {valor}", 
                        font=("Arial", 12, "bold"), 
                        bg="#2C3E50", 
                        fg="#3498DB").pack(pady=5)
        except KeyError:
            # EN CASO DE ERROR, LANZAMOS MENSAJE 
            messagebox.showerror("Error","No tienes nada registrado este día")

    # BOTON BUSCAR
    tk.Button(ventana, text="Buscar", command=show_date).pack(pady=10)

def ver_progreso():
    global ventana_progreso
    #Funcion para ver el progreso de los hábitos del día actual
    
    # VENTANA PARA PROGRESO
    ventana_progreso = tk.Toplevel()
    ventana_progreso.title("Progreso")
    ventana_progreso.geometry("400x400")
    ventana_progreso.configure(bg="#2C3E50")

    # LABEL PRINCIPAL TITULO
    tk.Label(ventana_progreso, 
            text=f"Progreso del día {fecha}", 
            font=("Arial", 16, "bold"), 
            fg="#ECF0F1", 
            bg="#2C3E50"
            ).pack(pady=15, padx=30) 
    
    # Por cada clave (habito) del diccionario, creamos una Label que muestra además el valor (estado)
    count = 0
    for clave, valor in historial[fecha].items(): 
        count += 1
        tk.Label(ventana_progreso, 
                text=f"{count}.  {clave.capitalize()}: {valor}", 
                font=("Arial", 12, "bold"), 
                bg="#2C3E50", 
                fg="#3498DB").pack(pady=5)

    def delete_all():
        global historial
        historial[fecha] = {}
        guardar_habitos(historial)
        messagebox.showinfo("Eliminar todos", "Todos los hábitos han sido eliminados.")
        ventana_progreso.destroy()
        ver_progreso()

    def complete_all():
        global historial
        for habito in historial[fecha]:
            historial[fecha][habito] = "Completado"
        guardar_habitos(historial)
        messagebox.showinfo("Completar todos", "Todos los hábitos han sido marcados como completados.")
        ventana_progreso.destroy()
        ver_progreso()

    # Boton para eliminar todos los hábitos
    tk.Button(ventana_progreso, 
              text="Eliminar todos", 
              command=delete_all, 
              bg="#E74C3C", 
              fg="#ECF0F1").pack(pady=10)

    # Boton para marcar todos los hábitos como completados
    tk.Button(ventana_progreso, 
              text="Completar todos", 
              command=complete_all, 
              bg="#E74C3C", 
              fg="#ECF0F1").pack(pady=10)

# === SECCIÓN: GUI ===

##Ventana Princpal
# - Ventana principal de la app, donde están alojados el titulo, la entrada de texto y los botones -
root = tk.Tk()
root.title("Easy Habit Tracker")
root.geometry("400x460")
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
                 ).pack(padx=10, pady=10)

mensaje = tk.Label(root, 
                 text=f"Escribe un hábito", 
                 font=("Arial", 12, "bold"), 
                 fg="#3498DB", 
                 bg="#2C3E50"
                 ).pack(padx=30, pady=5)

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

acciones = tk.Label(root, 
                 text=f"¿Que hacemos con tu hábito?", 
                 font=("Arial", 12, "bold"), 
                 fg="#3498DB", 
                 bg="#2C3E50"
                 ).pack(padx=30, pady=5)

##Botones de acción para hábitos

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


##Botones para visualizar datos

#Label aclaratorio
ver_progreso_historial = tk.Label(root, 
                 text=f"¿Quieres ver tu progreso?", 
                 font=("Arial", 12, "bold"), 
                 fg="#3498DB", 
                 bg="#2C3E50"
                 ).pack(padx=30, pady=5)

#Boton para ver progreso
boton_progreso = tk.Button(root, 
                   text="Ver progreso", 
                   command=ver_progreso, 
                   bg="#E74C3C", 
                   bd=0, 
                   fg="#ECF0F1").pack(pady=5)


#Boton para ver fechas anteriores
boton_progreso = tk.Button(root, 
                   text="Ver historial", 
                   command= ver_historial, 
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