from Entregable6.Models.AnimalModel import AnimalModel
from Entregable6.Views.AnimalView import AnimalView

import csv
from pathlib import Path


class AnimalController:

    def __init__(self):
        self.modelo = AnimalModel()
        self.vista = AnimalView()

    def listar_animales(self):
        animales = self.modelo.obtener_animales()
        self.vista.mostrar_animales(animales)

    def listar_especies(self, especie):
        animales = self.modelo.listar_especies(especie)
        self.vista.mostrar_mensaje("\nAnimales del refugio por Especie")
        print("*" * 44)
        self.vista.mostrar_animales(animales)

    def agregar_animales(self, nombre, especie, edad, adoptado):
        id = self.modelo.agregar_animales(nombre, especie, edad, adoptado)
        if id is not None:
            self.vista.mostrar_mensaje("Animal agregado al refugio ✔️")
        else:
            self.vista.mostrar_mensaje("Error al agregar animal al refugio ✖️")

    def adoptar_animal(self, id):
        done = self.modelo.adoptar_animal(id)
        if done is not None:
            self.vista.mostrar_mensaje("Animal adoptado! ✔️")
        else:
            self.vista.mostrar_mensaje("Error al adoptar animal al refugio ✖️")

    def eliminar_animal(self, id):
        done = self.modelo.eliminar_animal(id)
        if done is not None:
            self.vista.mostrar_mensaje("Animal eliminado! ✔️")
        else:
            self.vista.mostrar_mensaje("Error al eliminar animal al refugio ✖️")

    def obtener_ultimo(self):
        done = self.modelo.obtener_last_id()
        return done

    def guardar_csv(self):
        try:
            animales = self.modelo.obtener_animales()

            with open("Animales.csv", "w", newline="", encoding="utf-8") as csvfile:
                escritor = csv.writer(csvfile, delimiter=",")
                escritor.writerow(["Id", "Nombre", "Especie", "Edad", "Adoptado"])

                for animal in animales:
                    escritor.writerow([animal.id, animal.nombre, animal.especie, animal.edad, animal.adoptado])

            return self.vista.mostrar_mensaje("Archivo generado correctamente ✔️")

        except Exception as e:
            print(f"Error al guardar el CSV: {e} ️✖️")
            return self.vista.mostrar_mensaje("Archivo generado correctamente ✖️")

    def mostrar_menu(self):
        self.vista.mostrar_menu()
