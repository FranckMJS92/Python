from Classes.CentralTermica import CentralTermica
from Classes.CentralNuclear import CentralNuclear

"""
Clase para la colección de centrales
En ella se implementan los métodos para 
los cálculos del menú
"""
class ParqueGeneracion:
    def __init__(self):
        self.__centrales = []  # Lista de objetos Central

    def agregar_central(self, central):
        # Añade una central si no existe otra con el mismo nombre
        for existente in self.__centrales:
            if existente.nombre == central.nombre:
                return False
        self.__centrales.append(central)
        return True

    def mostrar_todas(self):
        # Devuelve un string con toda la información de las centrales
        if not self.__centrales:
            return "No hay centrales registradas."

        resultado = []
        for central in self.__centrales:
            resultado.append(str(central))
        return "\n".join(resultado)

    def produccion_total(self):
        # Devuelve la producción total de todas las centrales
        return sum(central.produccion_kwh for central in self.__centrales)

    def produccion_termicas(self):
        # Devuelve la producción total de las centrales térmicas
        return sum(central.produccion_kwh for central in self.__centrales
                   if isinstance(central, CentralTermica))

    def produccion_nucleares(self):
        # Devuelve la producción total de las centrales nucleares
        return sum(central.produccion_kwh for central in self.__centrales
                   if isinstance(central, CentralNuclear))

    def produccion_por_nombre(self, nombre):
        # Devuelve la producción de una central dado su nombre
        for central in self.__centrales:
            if central.nombre == nombre:
                return central.produccion_kwh
        return None

    def contar_termicas_por_combustible(self, tipo_combustible):
        # Cuenta cuántas centrales térmicas usan un combustible específico
        contador = 0
        for central in self.__centrales:
            if isinstance(central, CentralTermica) and central.combustible == tipo_combustible:
                contador += 1
        return contador

    def central_mayor_produccion(self):
        # Devuelve la central con mayor producción
        if not self.__centrales:
            return None
        return max(self.__centrales, key=lambda c: c.produccion_kwh)
