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

"""
sentenciaInsert = "INSERT INTO empleados (nombre, apellido, departamento, puesto, salario) VALUES (%s,%s,%s,%s,%s)"
valoresInsert = ("Paco","Perez","Desarrollo","Developer","12345")
cursor.execute(sentenciaInsert, valoresInsert)

# Realizamos commit para guardar los cambios
conexion.commit()

# Mostrar mensaje con el di generado
print("Registros afectados",cursor.rowcount)
print("Inserta con ID ",cursor.lastrowid)

# Insert con multiples
sentenciaInsert = "INSERT INTO empleados (nombre, apellido, departamento, puesto, salario) VALUES (%s,%s,%s,%s,%s)"
datos = [
    ("Carlos", "Alcantara", "Desarrollo", "Developer", "12345"),
    ("Daniel", "Carrillo", "Desarrollo", "Developer", "12345")
]

# Executemany
cursor.executemany(sentenciaInsert, datos)
conexion.commit()

# CRUD
consultaSelect = "SELECT * FROM empleados"
cursor.execute(consultaSelect)
resultado = cursor.fetchall()
for registro in resultado:
    print(registro)
"""
print("SELECT con WHERE")
consultaSelect = "SELECT * FROM empleados WHERE departamento = %s"
# usar una tupla aunque sea 1 solo valor
valor = ("Desarrollo",)
cursor.execute(consultaSelect, valor)
resultados = cursor.fetchall()
for registro in resultados:
    print(registro)

print("DELETE")
consultaDelete = "DELETE FROM empleados WHERE id = %s"
valorDelete = (13,)
cursor.execute(consultaDelete, valorDelete)
conexion.commit()
print("Registros borrados",cursor.rowcount)

print("UPDATE")
consultaUpdate = "UPDATE empleados SET departamento = %s WHERE id = %s"
valorUpdate = ("Department",14)
cursor.execute(consultaUpdate, valorUpdate)
conexion.commit()
print("Registros actualizados",cursor.rowcount)

# Buena practica
cursor.close()