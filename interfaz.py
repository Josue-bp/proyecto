import tkinter as tk
from tkinter import messagebox
import threading
import time
import os
from detector import detectar_rostros

# Estado de la detección
deteccion_activa = False

def iniciar_deteccion():
    global deteccion_activa
    if deteccion_activa:
        messagebox.showinfo("Aviso", "La detección ya está en curso.")
        return

    deteccion_activa = True
    estado.config(text="Estado: Detectando...", fg="green")

    def hilo_deteccion():
        try:
            detectar_rostros()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
        finally:
            estado.config(text="Estado: Inactivo", fg="red")
            global deteccion_activa
            deteccion_activa = False

    threading.Thread(target=hilo_deteccion, daemon=True).start()

def abrir_capturas():
    if os.path.exists("capturas"):
        os.startfile("capturas")
    else:
        messagebox.showwarning("Carpeta no encontrada", "La carpeta 'capturas' no existe.")

def abrir_registro():
    if os.path.exists("registro_detecciones.txt"):
        os.startfile("registro_detecciones.txt")
    else:
        messagebox.showwarning("Archivo no encontrado", "El archivo 'registro_detecciones.txt' no existe.")

def confirmar_salida():
    if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
        ventana.destroy()

def actualizar_hora():
    ahora = time.strftime("%d/%m/%Y %H:%M:%S")
    reloj.config(text=ahora)
    ventana.after(1000, actualizar_hora)

# Interfaz principal
ventana = tk.Tk()
ventana.title("Proyecto: Detección de Rostros")
ventana.geometry("320x280")
ventana.resizable(False, False)

# Título
tk.Label(ventana, text="Detección de Rostros", font=("Arial", 16)).pack(pady=10)

# Estado
estado = tk.Label(ventana, text="Estado: Inactivo", fg="red", font=("Arial", 12))
estado.pack(pady=5)

# Botones
tk.Button(ventana, text="Iniciar Cámara", width=25, command=iniciar_deteccion).pack(pady=5)
tk.Button(ventana, text="Ver Capturas", width=25, command=abrir_capturas).pack(pady=5)
tk.Button(ventana, text="Ver Registro", width=25, command=abrir_registro).pack(pady=5)
tk.Button(ventana, text="Salir", width=25, command=confirmar_salida).pack(pady=10)

# Reloj
reloj = tk.Label(ventana, text="", font=("Arial", 10))
reloj.pack()
actualizar_hora()

ventana.mainloop()



