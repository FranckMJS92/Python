"""
Clase Animal con atributos privados
Se crean getters y/o setters segun necesidad
"""

class Animal:
    """
    Clase que representa un animal en el refugio.
    Encapsula los atributos del animal y proporciona acceso controlado mediante propiedades.
    """

    def __init__(self, id: int, nombre, especie, edad: int, adoptado=False):
        """
        Constructor de la clase Animal.
        Args:
            id (int): Identificador único del animal (autoincremental en BD)
            nombre (str): Nombre del animal
            especie (str): Especie del animal (Perro, Gato, Conejo, etc.)
            edad (int): Edad del animal en años
            adoptado (bool): Estado de adopción, por defecto False (no adoptado)
        """
        self.__id = id              # Atributo privado: ID del animal
        self.__nombre = nombre      # Atributo privado: nombre del animal
        self.__especie = especie    # Atributo privado: especie del animal
        self.__edad = edad          # Atributo privado: edad en años
        self.__adoptado = adoptado  # Atributo privado: estado de adopción (True/False)

    @property
    def id(self):
        """
        Getter del ID.
        Returns:
            int: Identificador único del animal
        """
        return self.__id

    @property
    def nombre(self):
        """
        Getter del nombre.
        Returns:
            str: Nombre del animal
        """
        return self.__nombre

    @property
    def especie(self):
        """
        Getter de la especie.
        Returns:
            str: Especie del animal
        """
        return self.__especie

    @property
    def edad(self):
        """
        Getter de la edad.
        Returns:
            int: Edad del animal en años
        """
        return self.__edad

    @property
    def adoptado(self):
        """
        Getter del estado de adopción con formato legible.
        Returns:
            str: "Si" si está adoptado, "No" si no lo está
        """
        return "Si" if self.__adoptado else "No"

    # Metodo ToString
    def __str__(self):
        """
        Representación en string del objeto Animal.
        Formato: "ID | Nombre | Especie | Edad año(s) | Adoptado"
        Returns:
            str: Representación formateada del animal para mostrar al usuario
        """
        return f"{self.__id} | {self.__nombre} | {self.__especie} | {self.__edad} {"años" if self.__edad > 1 else "año"} | {"Sí" if self.__adoptado else "No"}"
