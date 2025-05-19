import tkinter as tk
import threading
from detector import detectar_rostros

# Función para correr detección sin bloquear la interfaz
def iniciar_deteccion():
    hilo = threading.Thread(target=detectar_rostros)
    hilo.start()

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Proyecto: Detección de Rostros")
ventana.geometry("300x200")

titulo = tk.Label(ventana, text="Detección de Rostros", font=("Arial", 14))
titulo.pack(pady=20)

btn_iniciar = tk.Button(ventana, text="Iniciar Cámara", command=iniciar_deteccion, width=20)
btn_iniciar.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, width=20)
btn_salir.pack(pady=5)

ventana.mainloop()
