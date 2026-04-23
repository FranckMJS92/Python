from Entregable5.Classes.Central import Central
from Entregable5.Enums.MaterialFisil import MaterialFisil

"""
Clase hereda de Central
material_fisil usa enum MaterialFisil
"""
class CentralNuclear(Central):
    # Constructor
    def __init__(self, nombre, ubicacion, produccion_kwh, material_fisil: MaterialFisil):
        # Se emplea el constructor del padre
        super().__init__(nombre, ubicacion, produccion_kwh)
        # Se agrega el atributo propio
        self.material_fisil = material_fisil

    # Metodo sobreescrito "to string"
    def __str__(self):
        return (f"Central Nuclear: '{self.nombre}' en {self.ubicacion} - "
                f"Producción: {self.produccion_kwh} kWh - Material: {self.material_fisil.value}")
