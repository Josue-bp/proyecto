import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import os
import time
from detector import detectar_rostros

# Función para correr detección sin bloquear la interfaz
def iniciar_deteccion():
    estado.config(text="Estado: Detectando...", fg="green")
    hilo = threading.Thread(target=detectar_rostros)
    hilo.start()

def abrir_capturas():
    os.startfile("capturas")

def abrir_registro():
    os.startfile("registro_detecciones.txt")

def confirmar_salida():
    if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
        ventana.quit()

def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")
    fecha_actual = time.strftime("%d/%m/%Y")
    reloj.config(text=f"{fecha_actual} {hora_actual}")
    ventana.after(1000, actualizar_hora)

# Cargar imágenes (se redimensionan)
def cargar_icono(ruta, tamaño=(24, 24)):
    imagen = Image.open(ruta)
    imagen = imagen.resize(tamaño, Image.ANTIALIAS)
    return ImageTk.PhotoImage(imagen)

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Proyecto: Detección de Rostros")
ventana.geometry("320x360")

# Cargar íconos
icono_camara = cargar_icono("iconos/camara-de-seguridad.png")
icono_detective = cargar_icono("iconos/detective.png")
icono_justicia = cargar_icono("iconos/palacio-de-justicia.png")

# Título
titulo = tk.Label(ventana, text="Detección de Rostros", font=("Arial", 14))
titulo.pack(pady=10)

# Estado
estado = tk.Label(ventana, text="Estado: Inactivo", fg="red", font=("Arial", 10))
estado.pack()

# Botones con íconos
btn_iniciar = tk.Button(ventana, text="  Iniciar Cámara", image=icono_camara, compound="left",
                        command=iniciar_deteccion, width=200, anchor="w")
btn_iniciar.pack(pady=10)

btn_capturas = tk.Button(ventana, text="  Ver Capturas", image=icono_detective, compound="left",
                         command=abrir_capturas, width=200, anchor="w")
btn_capturas.pack(pady=5)

btn_registro = tk.Button(ventana, text="  Ver Registro", image=icono_justicia, compound="left",
                         command=abrir_registro, width=200, anchor="w")
btn_registro.pack(pady=5)

btn_salir = tk.Button(ventana, text="Salir", command=confirmar_salida, width=20)
btn_salir.pack(pady=10)

# Reloj
reloj = tk.Label(ventana, text="", font=("Arial", 9))
reloj.pack()

# Iniciar reloj
actualizar_hora()

# Iniciar interfaz
ventana.mainloop()
