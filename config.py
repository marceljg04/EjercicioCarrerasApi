import mysql.connector

def get_db_connection():
    user = input("Introduce el usuario de la base de datos: ")
    password = input("Introduce la contraseña de la base de datos: ")
    return mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="universidad",
        ssl_disabled=True
    )