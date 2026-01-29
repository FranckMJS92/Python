class Coche:

    # Constructor
    # En los metodos de instancia, SELF es obligatorio al primer parametro

    # Visibilidad
    # atributo -> publico || _atributo -> protegido || __atributo -> privado
    def __init__(self, marca, modelo, km=0):
        self.marca = marca # self es lo mismo que this en java
        self.__modelo = modelo
        self.km = km

    # Metodos
    def mostrar(self):
        print(self.marca, self.modelo, self.km)

    # Getter y Setter en forma java
    def get_marca(self  ):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca


    # Formato python
    @property
    def modelo(self):
        return self.modelo

    @modelo.setter
    def modelo(self, modelo):
        self.modelo = modelo



    pass
