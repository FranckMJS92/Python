from Classes.CentralTermica import CentralTermica
from Classes.CentralNuclear import CentralNuclear
from Classes.ParqueGeneracion import ParqueGeneracion
from Enums.Combustible import Combustible
from Enums.MaterialFisil import MaterialFisil
from Utilities.Utilities import *


def mostrar_menu():
    print("\n" + "=" * 50)
    print("        GESTIÓN DE PRODUCCIÓN ELÉCTRICA")
    print("=" * 50)
    print("1. Añadir nueva central")
    print("2. Mostrar todas las centrales")
    print("3. Mostrar producción total (todas las centrales)")
    print("4. Mostrar producción total (centrales térmicas)")
    print("5. Mostrar producción total (centrales nucleares)")
    print("6. Mostrar producción de una central (por nombre)")
    print("7. Contar centrales térmicas por tipo de combustible")
    print("8. Mostrar central con mayor producción")
    print("9. Salir")
    print("=" * 50)


parque = ParqueGeneracion()

while True:
    mostrar_menu()
    opcion = pedir_entero("Elige una opción: ", minimo=1, maximo=9)

    if opcion == 1:
        if opcion == 1:
            print("\n--- AÑADIR NUEVA CENTRAL ---")
            tipo_termica = pedir_si_no("¿Es una central térmica?")

            nombre = pedir_cadena("Nombre: ")
            ubicacion = pedir_cadena("Ubicación: ")
            produccion = pedir_float("Producción (kWh): ", minimo=0)

            if tipo_termica:
                combustible = pedir_enum("Tipo de combustible", Combustible)
                central = CentralTermica(nombre, ubicacion, produccion, combustible)
            else:
                material = pedir_enum("Tipo de material físil", MaterialFisil)
                central = CentralNuclear(nombre, ubicacion, produccion, material)

            if parque.agregar_central(central):
                print(f"\n✅ Central '{nombre}' añadida correctamente")
            else:
                print(f"\n❌ Error: Ya existe una central con el nombre '{nombre}'")
        pass
    elif opcion == 2:
        print("\n" + parque.mostrar_todas())
    elif opcion == 3:
        print(f"\n⚡ Producción total: {parque.produccion_total()} kWh")
    elif opcion == 4:
        print(f"\n🔥 Producción total (térmicas): {parque.produccion_termicas()} kWh")
    elif opcion == 5:
        print(f"\n☢️ Producción total (nucleares): {parque.produccion_nucleares()} kWh")
    elif opcion == 6:
        nombre = pedir_cadena("Nombre de la central: ")
        produccion = parque.produccion_por_nombre(nombre)
        if produccion is None:
            print(f"\n❌ No se encontró la central '{nombre}'")
        else:
            print(f"\n⚡ Producción de '{nombre}': {produccion} kWh")
    elif opcion == 7:
        print("\nCombustibles disponibles:")
        combustible = pedir_enum("Selecciona combustible", Combustible)
        cantidad = parque.contar_termicas_por_combustible(combustible)
        print(f"\n🔢 Centrales térmicas que usan {combustible.value}: {cantidad}")
    elif opcion == 8:
        mejor = parque.central_mayor_produccion()
        if mejor is None:
            print("\n❌ No hay centrales registradas")
        else:
            print(f"\n🏆 Central con mayor producción:\n{mejor}")
    elif opcion == 9:
        print("\n🙋‍♂️ ¡Hasta luego!")
        break
