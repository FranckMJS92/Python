from Entregable6.Controllers.AnimalController import AnimalController
from Entregable6.Utilities.Utility import *

controlador = AnimalController()

while True:
    print()
    controlador.mostrar_menu()

    opcion = pedir_entero_rango("\nEscribe una opción: ", 1, 7)

    match opcion:
        case 1:
            controlador.listar_animales()
        case 2:
            especie = input("Indique la especie: ")
            controlador.listar_especies(especie)
        case 3:
            nombre = pedir_cadena("Escribe una nombre: ")
            especie = pedir_cadena("Escribe una especie: ")
            edad = pedir_entero_rango("Escribe su edad: ")
            adoptado = pedir_si_no("Está adoptado?: (Si/No) ")
            controlador.agregar_animales(nombre, especie, edad, adoptado)
        case 4:
            ultimo = controlador.obtener_ultimo()
            id = pedir_entero_rango("Indica el Id del animal adoptado: ", 1, ultimo)
            controlador.adoptar_animal(id)
        case 5:
            ultimo = controlador.obtener_ultimo()
            id = pedir_entero_rango("Indica el Id del animal eliminado del refugio: ", 1, ultimo)
            controlador.eliminar_animal(id)
        case 6:
            controlador.guardar_csv()
        case 7:
            break
        case _:
            print("Opcion invalida")
