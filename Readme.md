# 📷 Identificador de Rostros

Sistema de reconocimiento facial desarrollado en Python con PyQt6. Esta aplicación permite identificar rostros en tiempo real utilizando una interfaz gráfica amigable y funciones avanzadas de visión por computadora.

---

## ✨ Características Principales

- 👤 Inicio de sesión por reconocimiento facial
- 🎥 Detección de rostros en vivo usando la cámara web
- 💾 Registro automático de accesos y capturas
- 🖼️ Visualización de imágenes detectadas
- 📋 Acceso a historial de registros
- 🎛️ Interfaz moderna con PyQt6

---

## 🧰 Tecnologías Utilizadas

- 🐍 **Python 3.x** – Lenguaje principal
- 📷 **OpenCV** – Detección y reconocimiento facial
- 🎛️ **PyQt6** – Interfaz gráfica
- 🧠 **NumPy** – Procesamiento de datos
- 🗃️ **SQLite (opcional)** – Gestión de registros

---

## 🖥️ Interfaz de Usuario (GUI)

- **Botón:** 🟢 Iniciar Detector  
- **Botón:** 📋 Ver Registros  
- **Botón:** 🖼️ Abrir Capturas  
- **Área de cámara:** Vista en vivo con detección en tiempo real  
- **Menú superior:** Archivo, Ayuda, Salir

---

## 📂 Estructura del Proyecto

📦 IdentificadorRostros/
┣ 📂 captures/ # Imágenes de rostros capturados
┣ 📂 models/ # Modelos entrenados para reconocimiento
┣ 📂 ui/ # Archivos .ui de PyQt6 o .py generados
┣ 📜 main.py # Punto de entrada principal
┣ 📜 detector.py # Lógica de detección y reconocimiento
┣ 📜 registro.py # Manejo de registros de acceso
┣ 📜 database.py # Conexión a base de datos SQLite
┣ 📜 utils.py # Funciones auxiliares (opcional)
┗ 📜 README.md

yaml
Copiar
Editar

---

## ⚙️ Requisitos Previos

Antes de ejecutar el sistema, asegúrate de tener instalado:

- Python 3.9+
- pip (gestor de paquetes)
- Cámara web funcional

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt