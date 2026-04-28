from Entregable6.Models.AnimalModel import AnimalModel
from Entregable6.Views.AnimalView import AnimalView

import csv

class AnimalController:
    """
    Controlador principal de la aplicación.
    Actúa como intermediario entre el Modelo (BD) y la Vista (interfaz de usuario).
    Aplica la lógica de negocio y coordina las operaciones.
    """

    def __init__(self):
        """
        Constructor del controlador.
        Inicializa las instancias del modelo y la vista.
        """
        self.modelo = AnimalModel()  # Capa de acceso a datos
        self.vista = AnimalView()  # Capa de presentación

    def listar_animales(self):
        """
        Obtiene todos los animales del modelo y los envía a la vista para mostrar.
        """
        animales = self.modelo.obtener_animales()
        self.vista.mostrar_animales(animales)

    def listar_especies(self, especie):
        """
        Filtra animales por especie y los muestra.
        Args:
            especie (str): Especie a filtrar (ej: "Perro", "Gato")
        """
        animales = self.modelo.listar_especies(especie)
        self.vista.mostrar_mensaje("\nAnimales del refugio por Especie")
        print("*" * 44)
        self.vista.mostrar_animales(animales)

    def agregar_animal(self, nombre, especie, edad, adoptado):
        """
        Agrega un nuevo animal al refugio.
        Args:
            nombre (str): Nombre del animal
            especie (str): Especie del animal
            edad (int): Edad en años
            adoptado (bool): Estado de adopción inicial
        """
        id = self.modelo.agregar_animal(nombre, especie, edad, adoptado)
        if id is not None:
            self.vista.mostrar_mensaje("Animal agregado al refugio ✔️")
        else:
            self.vista.mostrar_mensaje("Error al agregar animal al refugio ✖️")

    def adoptar_animal(self, id):
        """
        Marca un animal como adoptado.
        Args:
            id (int): ID del animal a adoptar
        """
        done = self.modelo.adoptar_animal(id)
        if done is not None:
            self.vista.mostrar_mensaje("Animal adoptado! ✔️")
        else:
            self.vista.mostrar_mensaje("Error al adoptar animal al refugio ✖️")

    def eliminar_animal(self, id):
        """
        Elimina un animal del refugio.
        Args:
            id (int): ID del animal a eliminar
        """
        done = self.modelo.eliminar_animal(id)
        if done is not None:
            self.vista.mostrar_mensaje("Animal eliminado! ✔️")
        else:
            self.vista.mostrar_mensaje("Error al eliminar animal al refugio ✖️")

    def obtener_ultimo(self):
        """
        Obtiene el último ID registrado en la base de datos.
        Returns:
            int | done: El último ID o None si no hay registros
        """
        done = self.modelo.obtener_last_id()
        return done

    def guardar_csv(self):
        """
        Exporta todos los animales a un archivo CSV.
        El archivo se sobrescribe cada vez (modo "w").
        Returns:
            bool: True si se guardó correctamente, False si hubo error
        """
        try:
            animales = self.modelo.obtener_animales()

            with open("Animales.csv", "w", newline="", encoding="utf-8") as csvfile:
                escritor = csv.writer(csvfile, delimiter=",")
                # Cabecera del CSV
                escritor.writerow(["Id", "Nombre", "Especie", "Edad", "Adoptado"])

                # Escribe cada animal como una fila
                for animal in animales:
                    escritor.writerow([animal.id, animal.nombre, animal.especie, animal.edad, animal.adoptado])

            return self.vista.mostrar_mensaje("Archivo generado correctamente ✔️")

        except Exception as e:
            print(f"Error al guardar el CSV: {e} ✖️")
            return self.vista.mostrar_mensaje("Error al generar el archivo ✖️")

    def mostrar_menu(self):
        """
        Muestra el menú principal al usuario delegando en la vista.
        """
        self.vista.mostrar_menu()
