import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='empresa'
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # conexion.close()
    print("CONEXION EXITOSA")

# OObtenemos el cursos para poder ejecutar consultas
cursor = conexion.cursor()

sentenciaInsert = "INSERT INTO empleados (nombre, apellido, departamento, puesto, salario) VALUES (%s,%s,%s,%s,%s)"
valoresInsert = ("Paco","Perez","Desarrollo","Developer","12345")
cursor.execute(sentenciaInsert, valoresInsert)

# Realizamos commit para guardar los cambios
conexion.commit()

# Mostrar mensaje con el di generado
print("Registros afectados",cursor.rowcount)
print("Inserta con ID ",cursor.lastrowid)
