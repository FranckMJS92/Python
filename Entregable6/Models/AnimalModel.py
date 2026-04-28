from Entregable6.Models.Animal import Animal
from Entregable6.conexion import crear_conexion

'''
Clase AnimalModel contiene los metodos para la comunicacion con BBDD
'''

class AnimalModel:
    """
    Modelo para la gestión de la tabla 'animales' en la base de datos.
    Encapsula todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
    """
    def obtener_animales(self):
        """
        Obtiene todos los animales de la base de datos.
        Returns:
            list[Animal]: Lista de objetos Animal ordenados por ID.
                          Retorna lista vacía si no hay conexión o no hay datos.
        """
        conexion = crear_conexion()
        animales = []

        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales ORDER BY id")
            for a in cursor.fetchall():
                animales.append(Animal(*a))  # Desempaqueta la tupla para crear el objeto
            conexion.close()

        return animales

    def listar_especies(self, especie):
        """
        Filtra animales por especie específica.
        Args:
            especie (str): Nombre de la especie a filtrar (ej: "Perro", "Gato")
        Returns:
            list[Animal]: Lista de animales de la especie indicada.
                          Retorna lista vacía si no hay conexión o no hay coincidencias.
        """
        conexion = crear_conexion()
        especies = []

        if conexion:
            cursor = conexion.cursor()
            # Uso de parámetro %s para prevenir inyección SQL
            cursor.execute("SELECT * FROM animales WHERE especie = %s ORDER BY id", (especie,))
            for a in cursor.fetchall():
                especies.append(Animal(*a))
            conexion.close()

        return especies

    def agregar_animal(self, nombre, especie, edad, adoptado=False):
        """
        Inserta un nuevo animal en la base de datos.
        Args:
            nombre (str): Nombre del animal
            especie (str): Especie del animal
            edad (int): Edad en años
            adoptado (bool): Estado de adopción, por defecto False
        Returns:
            int | None: El ID auto-generado del nuevo registro, o None si falló la conexión
        """
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sqlInsert = "INSERT INTO animales(nombre, especie, edad, adoptado) VALUES (%s, %s, %s, %s)"
            valoresInsert = (nombre, especie, edad, adoptado)
            cursor.execute(sqlInsert, valoresInsert)
            conexion.commit()  # Importante: confirma la transacción
            ultimo_id = cursor.lastrowid  # Obtiene el ID generado por AUTO_INCREMENT
            conexion.close()
            return ultimo_id
        else:
            return None

    def adoptar_animal(self, id):
        """
        Marca un animal como adoptado (cambia adoptado a True).
        Args:
            id (int): ID del animal a adoptar
        Returns:
            bool: True si la actualización fue exitosa, False si falló la conexión
        """
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
        """
        Elimina un animal de la base de datos por su ID.
        Args:
            id (int): ID del animal a eliminar
        Returns:
            bool: True si la eliminación fue exitosa, False si falló la conexión
        """
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
        """
        Obtiene el ID más alto (último registro insertado).
        Returns:
            int | None: El último ID registrado, o None si no hay conexión o tabla vacía
        """
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchone()  # Mejor que fetchall() para un solo registro
            conexion.close()
            return resultado[0] if resultado else None  # Retorna None si no hay registros
        else:
            return None
