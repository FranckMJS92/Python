"""
Módulo de conexión a la base de datos MySQL.
Proporciona una función para establecer y gestionar la conexión con la BBDD.
"""

import mysql.connector
from config import *

# Constantes de configuración importadas desde config.py:
# DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def crear_conexion():
    """
    Crea y devuelve una conexión a la base de datos MySQL.
    Utiliza los parámetros de conexión definidos en el archivo config.py:
    - DB_HOST: Dirección del servidor (ej: localhost)
    - DB_PORT: Puerto de conexión (ej: 3306)
    - DB_USER: Usuario de la base de datos
    - DB_PASSWORD: Contraseña del usuario
    - DB_NAME: Nombre de la base de datos a conectar
    Returns:
        mysql.connector.connection.MySQLConnection | None: 
            Objeto de conexión si es exitosa, None si ocurre un error.
    Example:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM tabla")
            # ... operaciones ...
            conexion.close()
    Note:
        Es responsabilidad del llamador cerrar la conexión cuando ya no sea necesaria.
    """
    try:
        # Intenta establecer conexión con los parámetros de configuración
        mydb = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return mydb  # Conexión exitosa
    except mysql.connector.Error as err:
        # Captura cualquier error específico de MySQL
        print(f"Error de conexión a MySQL: {err}")
        return None  # Retorna None para indicar que falló la conexión
    except Exception as e:
        # Captura cualquier otro error inesperado (opcional pero recomendado)
        print(f"Error inesperado al conectar a la base de datos: {e}")
        return None
