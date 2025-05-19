import sys
import subprocess
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QStatusBar, QLineEdit
)
from PyQt6.QtCore import Qt

# Base de usuarios simple (puedes cambiar esto por una DB después)
USUARIOS = {
    "admin": "1234",
    "josue": "clave"
}

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(650, 350, 350, 250)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Inicia sesión para continuar")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        layout.addWidget(self.usuario)

        self.clave = QLineEdit()
        self.clave.setPlaceholderText("Contraseña")
        self.clave.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.clave)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.verificar_login)
        layout.addWidget(self.login_button)

        self.status = QStatusBar()
        layout.addWidget(self.status)

        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: white;
                font-family: Arial;
            }
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border-radius: 6px;
                background-color: #ECEFF4;
                color: black;
            }
            QPushButton {
                background-color: #5E81AC;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C6996;
            }
        """)

        self.setLayout(layout)

    def verificar_login(self):
        usuario = self.usuario.text()
        clave = self.clave.text()
        if usuario in USUARIOS and USUARIOS[usuario] == clave:
            self.status.showMessage(f"Bienvenido, {usuario}")
            self.close()
            self.ventana_principal = MainWindow()
            self.ventana_principal.show()
        else:
            self.status.showMessage("Usuario o contraseña incorrectos")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyecto: Detector Facial")
        self.setGeometry(600, 300, 400, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Bienvenido a la Detección de Rostros")
        self.label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Iniciar Detección")
        self.button.clicked.connect(self.ejecutar_detector)
        layout.addWidget(self.button)

        self.ver_registro = QPushButton("Ver Registro de Detecciones")
        self.ver_registro.clicked.connect(self.abrir_registro)
        layout.addWidget(self.ver_registro)

        self.abrir_carpeta = QPushButton("Abrir Carpeta de Capturas")
        self.abrir_carpeta.clicked.connect(self.abrir_capturas)
        layout.addWidget(self.abrir_carpeta)

        self.status = QStatusBar()
        self.status.showMessage("Listo para iniciar detección")
        layout.addWidget(self.status)

        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: white;
                font-family: Arial;
            }
            QPushButton {
                background-color: #5E81AC;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C6996;
            }
        """)

        self.setLayout(layout)

    def ejecutar_detector(self):
        self.status.showMessage("Ejecutando detector...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        detector_path = os.path.join(script_dir, "detector.py")

        if os.path.exists(detector_path):
            subprocess.Popen([sys.executable, detector_path])
            self.status.showMessage("Detector iniciado")
        else:
            self.status.showMessage("No se encontró detector.py")

    def abrir_registro(self):
        registro_path = os.path.join(os.path.dirname(__file__), "registro_detecciones.txt")
        if os.path.exists(registro_path):
            subprocess.Popen(["notepad.exe", registro_path])
        else:
            self.status.showMessage("No hay registro aún.")

    def abrir_capturas(self):
        capturas_path = os.path.join(os.path.dirname(__file__), "capturas")
        if not os.path.exists(capturas_path):
            os.makedirs(capturas_path)
        os.startfile(capturas_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
