import cv2
from datetime import datetime, timedelta
import os

# Rutas
base_dir = os.path.dirname(os.path.abspath(__file__))
capturas_dir = os.path.join(base_dir, "capturas")
registro_path = os.path.join(base_dir, "registro_detecciones.txt")

if not os.path.exists(capturas_dir):
    os.makedirs(capturas_dir)

# Detector y cámara
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

ultimo_guardado = datetime.now() - timedelta(seconds=5)
contador_detecciones = 0

#  Punto de grabación
def draw_rec(frame):
    cv2.circle(frame, (30, 30), 8, (0, 0, 255), -1)
    cv2.putText(frame, "REC", (50, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = detector.detectMultiScale(gris, 1.3, 5)

    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Rojo

    # Texto de fecha y detecciones
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, f"{fecha_hora}", (400, 460), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 255), 1)
    cv2.putText(frame, f"Detecciones: {contador_detecciones}", (10, 460), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 255), 1)

    draw_rec(frame)  #  "REC"

    # Guardar captura si han pasado 5s y hay rostros
    if len(rostros) > 0 and datetime.now() - ultimo_guardado > timedelta(seconds=5):
        fecha_hora_archivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"terror_{fecha_hora_archivo}.jpg"
        ruta_guardado = os.path.join(capturas_dir, nombre_archivo)

        cv2.imwrite(ruta_guardado, frame)
        print(f"[ Imagen guardada]: {ruta_guardado}")
        contador_detecciones += 1
        ultimo_guardado = datetime.now()

        with open(registro_path, "a") as f:
            f.write(f"{fecha_hora} - Detección: {len(rostros)} rostro(s) - Imagen: {ruta_guardado}\n")

    cv2.imshow(' CAMARA DE TERROR', frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cam.release()
cv2.destroyAllWindows()