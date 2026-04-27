'''
Clase Animal con atributos privados
Se crean getters y/o setters segun necesidad
'''


class Animal:
    def __init__(self, id: int, nombre, especie, edad: int, adoptado=False):
        self.__id = id
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__adoptado = adoptado

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def especie(self):
        return self.__especie

    @property
    def edad(self):
        return self.__edad

    @property
    def adoptado(self):
        return "Si" if self.__adoptado else "No"

    # Metodo ToString
    def __str__(self):
        return f"{self.__id} | {self.__nombre} | {self.__especie} | {self.__edad} {"años" if self.__edad > 1 else "año"} | {"Sí" if self.__adoptado else "No"}"
