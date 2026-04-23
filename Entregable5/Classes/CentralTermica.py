from Entregable5.Classes.Central import Central
from Enums.Combustible import Combustible

"""
Clase hereda de Central
combustible usa enum Combustible
"""
class CentralTermica(Central):
    # Constructor
    def __init__(self, nombre, ubicacion, produccion_kwh, combustible: Combustible):
        # Se emplea el constructor del padre
        super().__init__(nombre, ubicacion, produccion_kwh)
        # Se agrega el atributo propio
        self.__combustible = combustible

    # Getter
    @property
    def combustible(self):
        return self.__combustible

    # Metodo sobreescrito "to string"
    def __str__(self):
        return (f"Central Térmica: '{self.nombre}' en {self.ubicacion} - "
                f"Producción: {self.produccion_kwh} kWh - Combustible: {self.combustible.value}")
