READ ME


Estructura del Proyecto
-----------------------
ProyectoCarreras/
│
├── app.py               # Servidor Flask (API REST)
├── main.py              # Cliente en consola
├── Carrera.py           # Clase modelo de datos
├── CarreraDAO.py        # Capa de acceso a datos (DAO)
├── config.py            # Configuración de conexión a MySQL
└── README.md            # Documentación del proyecto

Configuración de la Base de Datos
---------------------------------
Abrir MySQL y ejecutar el siguiente script SQL:

CREATE DATABASE universidad;
USE universidad;

CREATE TABLE carrera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

Configuración de la Conexión (config.py)
----------------------------------------
El archivo config.py contiene la configuración de conexión a la base de datos:

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="universidad",
        ssl_disabled=True
    )

Instalación de librerias
------------------------
pip install flask
pip install mysql-connector-python
pip install requests


Ejecución del Proyecto
---------------------
Iniciar la API
Desde la terminal ejecutar:

py -m flask --app CarreraAPI run
Si la conexión es exitosa, se muestra un mensaje como:

✅ Conexión exitosa a MySQL
 * Running on http://127.0.0.1:5000

Iniciar el Cliente en Consola
En otra terminal, ejecutar el siguiente comando o bien desde interfaz del VS correr el programa:

python main.py

Ya estaria preparada la aplicación