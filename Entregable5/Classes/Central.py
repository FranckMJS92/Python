from abc import ABC, abstractmethod

# Clase abstracta para cualquier tipo de central
class Central(ABC):

    # Constructor
    def __init__(self, nombre, ubicacion, produccion_kwh):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__produccion_kwh = produccion_kwh

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def ubicacion(self):
        return self.__ubicacion

    @property
    def produccion_kwh(self):
        return self.__produccion_kwh

    @abstractmethod
    def __str__(self):
        # Sobreescrita en las clases hijas
        pass
