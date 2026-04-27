from Entregable6.Models.Animal import Animal
from Entregable6.conexion import crear_conexion

'''
Clase AnimalModel contiene los metodos para la comunicacion con BBDD
'''

class AnimalModel:

    def obtener_animales(self):
        conexion = crear_conexion()
        animales = []

        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales ORDER BY id")
            for a in cursor.fetchall():
                animales.append(Animal(*a))

        conexion.close()
        return animales

    def listar_especies(self, especie):
        conexion = crear_conexion()
        especies = []

        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales WHERE especie = %s ORDER BY id", (especie,))
            for a in cursor.fetchall():
                especies.append(Animal(*a))

        conexion.close()
        return especies

    def agregar_animales(self, nombre, especie, edad, adoptado=False):
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sqlInsert = "INSERT INTO animales(nombre, especie, edad, adoptado) VALUES (%s, %s, %s, %s)"
            valoresInsert = (nombre, especie, edad, adoptado)
            cursor.execute(sqlInsert, valoresInsert)
            conexion.commit()
            conexion.close()
            return cursor.lastrowid
        else:
            return None

    def adoptar_animal(self, id):
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sqlUpdate = "UPDATE animales SET adoptado = True WHERE id = %s"
            valoresUpdate = (id,)
            cursor.execute(sqlUpdate, valoresUpdate)
            conexion.commit()
            conexion.close()
            return True
        else:
            return False

    def eliminar_animal(self, id):
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            sqlDelete = "DELETE FROM animales WHERE id = %s"
            valoresDelete = (id,)
            cursor.execute(sqlDelete, valoresDelete)
            conexion.commit()
            conexion.close()
            return True
        else:
            return False

    def obtener_last_id(self):
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales ORDER BY id DESC LIMIT 1")
            for a in cursor.fetchall():
                return a[0]
        else:
            return None