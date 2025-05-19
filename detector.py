import cv2
from datetime import datetime, timedelta
import os

# Obtener la ruta absoluta del directorio donde está este archivo
base_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la carpeta "capturas"
capturas_dir = os.path.join(base_dir, "capturas")

# Crear la carpeta si no existe
if not os.path.exists(capturas_dir):
    os.makedirs(capturas_dir)

# Ruta completa para el registro de detecciones
registro_path = os.path.join(base_dir, "registro_detecciones.txt")

# Configuración del detector y cámara
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

# Variables para control de tiempo y conteo
ultimo_guardado = datetime.now() - timedelta(seconds=5)
contador_detecciones = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = detector.detectMultiScale(gris, 1.3, 5)

    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, fecha_hora, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Detecciones: {contador_detecciones}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Guardar captura si ha pasado suficiente tiempo desde la última
    if len(rostros) > 0 and datetime.now() - ultimo_guardado > timedelta(seconds=5):
        fecha_hora_archivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"captura_{fecha_hora_archivo}.jpg"
        ruta_guardado = os.path.join(capturas_dir, nombre_archivo)

        cv2.imwrite(ruta_guardado, frame)
        print(f"Imagen guardada: {ruta_guardado}")
        contador_detecciones += 1
        ultimo_guardado = datetime.now()

        with open(registro_path, "a") as f:
            f.write(f"{fecha_hora} - Detección: {len(rostros)} rostro(s) - Imagen: {ruta_guardado}\n")

    cv2.imshow('Detección de Rostros', frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cam.release()
cv2.destroyAllWindows()