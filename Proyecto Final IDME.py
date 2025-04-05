import tkinter as tk  # Interfaz gráfica
from tkinter import messagebox  # Ventanas emergentes
import sqlite3  # Base de datos
import calendar  # Mostrar calendario
from datetime import datetime  # Obtener fecha actual

#  Conexión a la base de datos SQLite
conn = sqlite3.connect("recordatorios.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS recordatorios (
                    id INTEGER PRIMARY KEY, 
                    fecha TEXT, 
                    mensaje TEXT)''')
conn.commit()  # Guarda cambios en la base de datos

#  Función para agregar un recordatorio a la base de datos
def agregar_recordatorio():
    fecha = entry_fecha.get()  # Obtiene la fecha ingresada
    mensaje = entry_mensaje.get()  # Obtiene el mensaje ingresado
    
    if fecha and mensaje:  # Verifica que los campos no estén vacíos
        cursor.execute("INSERT INTO recordatorios (fecha, mensaje) VALUES (?, ?)", (fecha, mensaje))
        conn.commit()  # Guarda cambios en la base de datos
        entry_fecha.delete(0, tk.END)  # Limpia la caja de texto de fecha
        entry_mensaje.delete(0, tk.END)  # Limpia la caja de texto de mensaje
        actualizar_lista()  # Actualiza la lista de recordatorios
        messagebox.showinfo("Éxito", "Recordatorio agregado.")  # Mensaje de confirmación
    else:
        messagebox.showerror("Error", "Ingrese fecha y mensaje.")  # Muestra error si falta info

#  Función para actualizar la lista de recordatorios en la interfaz
def actualizar_lista():
    lista.delete(0, tk.END)  # Limpia la lista antes de actualizar
    cursor.execute("SELECT fecha, mensaje FROM recordatorios ORDER BY fecha")
    for row in cursor.fetchall():  # Recorre los datos y los muestra en la lista
        lista.insert(tk.END, f"{row[0]} - {row[1]}")

#  Función para mostrar el calendario del año actual en una ventana emergente
def mostrar_calendario():
    year = datetime.now().year  # Obtiene el año actual
    cal = calendar.TextCalendar()  # Crea un calendario en texto
    cal_str = cal.formatyear(year)  # Formatea el calendario del año en texto
    messagebox.showinfo(f"Calendario {year}", cal_str)  # Muestra el calendario en una ventana emergente

#  Creación de la interfaz gráfica con Tkinter
root = tk.Tk()  # Inicializa la ventana principal
root.title("Calendario con Recordatorios")  # Título de la ventana

#  Campos de entrada para la fecha y el mensaje del recordatorio
tk.Label(root, text="Fecha (YYYY-MM-DD):").pack()  # Etiqueta de fecha
entry_fecha = tk.Entry(root)  # Caja de texto para ingresar la fecha
entry_fecha.pack()

tk.Label(root, text="Mensaje:").pack()  # Etiqueta del mensaje
entry_mensaje = tk.Entry(root, width=50)  # Caja de texto para ingresar el mensaje
entry_mensaje.pack()

#  Botones para agregar recordatorio y mostrar calendario
tk.Button(root, text="Agregar Recordatorio", command=agregar_recordatorio).pack()
tk.Button(root, text="Mostrar Calendario", command=mostrar_calendario).pack()

#  Lista donde se mostrarán los recordatorios guardados
lista = tk.Listbox(root, width=50, height=10)
lista.pack()
actualizar_lista()  # Carga los recordatorios existentes al iniciar

#  Ejecuta la aplicación gráfica
root.mainloop()