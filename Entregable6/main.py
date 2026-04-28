"""
Archivo principal del programa.
Punto de entrada de la aplicación que implementa el bucle principal del menú.
"""
from Entregable6.Controllers.AnimalController import AnimalController
from Entregable6.Utilities.Utility import *

# Instancia única del controlador principal
controlador = AnimalController()

# Bucle principal del programa
while True:
    print()  # Línea en blanco para separar iteraciones
    controlador.mostrar_menu()

    # Solicita una opción válida entre 1 y 7
    opcion = pedir_entero_rango("\nEscribe una opción: ", 1, 7)

    # Estructura match-case (Python 3.10+)
    match opcion:
        case 1:
            # Listar todos los animales del refugio
            controlador.listar_animales()

        case 2:
            # Buscar animales por especie
            especie = pedir_cadena("Indique la especie: ")
            controlador.listar_especies(especie)

        case 3:
            # Agregar un nuevo animal
            nombre = pedir_cadena("Escribe un nombre: ")
            especie = pedir_cadena("Escribe una especie: ")
            edad = pedir_entero_rango("Escribe su edad: ")  # Usa valores por defecto (min=0, max=100)
            adoptado = pedir_si_no("¿Está adoptado? (Si/No): ")
            controlador.agregar_animal(nombre, especie, edad, adoptado)

        case 4:
            # Adoptar un animal existente
            ultimo = controlador.obtener_ultimo()
            if ultimo is not None and ultimo > 0:
                id = pedir_entero_rango("Indica el Id del animal adoptado: ", 1, ultimo)
                controlador.adoptar_animal(id)
            else:
                print("⚠️ No hay animales registrados en el refugio.")

        case 5:
            # Eliminar un animal del refugio
            ultimo = controlador.obtener_ultimo()
            if ultimo is not None and ultimo > 0:
                id = pedir_entero_rango("Indica el Id del animal a eliminar del refugio: ", 1, ultimo)
                controlador.eliminar_animal(id)
            else:
                print("⚠️ No hay animales para eliminar.")

        case 6:
            # Exportar datos a archivo CSV
            controlador.guardar_csv()

        case 7:
            # Salir del programa
            print("¡Hasta luego! 👋")
            break

        case _:
            # Opción no contemplada
            print("Opción inválida")
