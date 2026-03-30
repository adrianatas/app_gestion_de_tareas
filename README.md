# App de Gestión de Tareas

Una app simple para apuntar tareas por **nombre, fecha y categoría**, con opción de **guardar, modificar y eliminar**.  
La interfaz está construida con **HTML, CSS y JS de Bootstrap** y el backend es con **Flask y SQLAlchemy**.

---

## Estructura del proyecto

M6_01
├─ main.py # archivo principal de Flask
├─ db.py # configuración de la base de datos
├─ models.py # modelos de datos
├─ templates/ # archivos HTML
├─ static/ # CSS, JS, imágenes
├─ .gitignore
├─ requirements.txt
└─ README.md


---

##  Requisitos

- Python 3.12  
- Flask 3.1.2  
- SQLAlchemy 2.0.44

Todos los paquetes están listados en `requirements.txt`.

---

##  Instalación

1. Clonar el repositorio:

git clone https://github.com/adrianatas/app_gestion_de_tareas.git
cd app_gestion_tareas

# Crear un entorno virtual
python -m venv .venv

# Activar el entorno virtual Windows PowerShell
.venv\Scripts\activate
#Instalar dependencias
pip install -r requirements.txt
#Ejecutar la aplicación
python main.py

# Base de datos y notas 
La app usa SQLite y crea automáticamente la base de datos local al iniciar.
Cada usuario tendrá su propia base de datos, así los datos son locales y privados.

.venv y archivos temporales están ignorados con .gitignore
Puedes hacer tus propios cambios y commits para mantener el historial limpio
Cada usuario tendrá su propia base de datos, así los datos son locales y privados.
