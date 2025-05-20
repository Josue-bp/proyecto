import sys
import subprocess
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QStatusBar, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QPixmap, QIcon, QMovie
from PyQt6.QtCore import Qt, QSize

USUARIOS = {
    "admin": "1234",
    "josue": "clave",
    "flavio": "12345"
}

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(650, 350, 350, 300)
        self.setStyleSheet("background-color: #2E3440; color: white; font-family: Arial;")

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)
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
                padding: 10px;
                font-size: 14px;
                border-radius: 6px;
                background-color: #ECEFF4;
                color: black;
                border: 2px solid #81A1C1;
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
            QMessageBox.warning(self, "Error de Autenticación", "Usuario o contraseña incorrectos")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyecto: Detector Facial")
        self.setGeometry(600, 300, 460, 460)

        # GIF de fondo
        self.fondo_gif = QLabel(self)
        self.fondo_gif.setGeometry(0, 0, self.width(), self.height())
        self.fondo_gif.setScaledContents(True)
        movie = QMovie("iconos/carro.gif")
        self.fondo_gif.setMovie(movie)
        movie.start()

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Bienvenido a la Detección de Rostros")
        self.label.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #ECEFF4;
            text-shadow: 2px 2px 4px #2E3440;
        """)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        if os.path.exists("logo.png"):
            imagen = QLabel()
            imagen.setPixmap(QPixmap("logo.png").scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(imagen)

        botones = [
            ("Iniciar Detección", "iconos/huella-dactilar.png", self.ejecutar_detector),
            ("Ver Registro de Detecciones", "iconos/lupa.png", self.abrir_registro),
            ("Abrir Carpeta de Capturas", "iconos/sospechar.png", self.abrir_capturas),
            ("Salir", "iconos/linea-policial.png", self.salir_app)
        ]

        for texto, ruta_icono, func in botones:
            btn = QPushButton(texto)
            btn.setFixedHeight(50)
            if os.path.exists(ruta_icono):
                btn.setIcon(QIcon(ruta_icono))
            btn.setIconSize(QSize(28, 28))
            btn.clicked.connect(func)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #5E81AC;
                    color: white;
                    font-size: 18px;
                    font-weight: 600;
                    border-radius: 20px;
                    box-shadow: 0 5px 10px rgba(0,0,0,0.35);
                    padding-left: 10px;
                    padding-right: 10px;
                    qproperty-iconSize: 28px 28px;
                }
                QPushButton:hover {
                    background-color: #81A1C1;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.45);
                }
                QPushButton:pressed {
                    background-color: #4C6996;
                }
            """)
            btn.setStyleSheet(btn.styleSheet() + """
                QPushButton {
                    text-align: center;
                }
            """)
            layout.addWidget(btn)

        self.status = QStatusBar()
        self.status.showMessage("Listo para iniciar detección")
        layout.addWidget(self.status)

        self.setLayout(layout)

        # Poner el GIF detrás de los widgets
        self.fondo_gif.lower()

        self.setStyleSheet("""
            QWidget {
                background: transparent;
                color: #D8DEE9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QStatusBar {
                background: transparent;
                color: #D8DEE9;
                font-style: italic;
            }
        """)

    def resizeEvent(self, event):
        self.fondo_gif.setGeometry(0, 0, self.width(), self.height())
        return super().resizeEvent(event)

    def ejecutar_detector(self):
        try:
            self.status.showMessage("Ejecutando detector...")
            subprocess.Popen([sys.executable, "detector.py"])
            self.status.showMessage("Detector iniciado")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo iniciar el detector:\n{e}")

    def abrir_registro(self):
        if os.path.exists("registro_detecciones.txt"):
            subprocess.Popen(["notepad.exe", "registro_detecciones.txt"])
        else:
            QMessageBox.information(self, "Registro no encontrado", "No hay registro aún.")

    def abrir_capturas(self):
        try:
            if not os.path.exists("capturas"):
                os.makedirs("capturas")
            os.startfile("capturas")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir la carpeta:\n{e}")

    def salir_app(self):
        respuesta = QMessageBox.question(
            self, "Salir", "¿Seguro que quieres salir?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta == QMessageBox.StandardButton.Yes:
            QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
