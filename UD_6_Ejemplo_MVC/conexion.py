import mysql.connector

from config import *

def crear_conexion():
    try:
        mydb = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # conexion.close()
        print("CONEXION EXITOSA")