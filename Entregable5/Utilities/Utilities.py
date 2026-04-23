"""
Menu para solicitar peticiones al usuario
"""
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

"""
Pide una cadena al usuario.
No permite cadenas vacías o solo espacios.
"""
def pedir_cadena(mensaje):
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                raise ValueError("La entrada no puede estar vacía")
            return valor.upper()
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")


"""Pide un entero. Si minimo/maximo no son None, valida el rango."""
def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = input(mensaje)
            if not valor.strip():
                raise ValueError("No se permite entrada vacía")

            entero = int(valor)

            if minimo is not None and entero < minimo:
                raise ValueError(f"El número debe ser mayor o igual a {minimo}")
            if maximo is not None and entero > maximo:
                raise ValueError(f"El número debe ser menor o igual a {maximo}")

            return entero
        except ValueError:
            print("El valor no es un número")


"""Pide un flotante. Si minimo/maximo no son None, valida el rango."""
def pedir_float(mensaje, minimo, maximo=None):
    while True:
        try:
            valor = input(mensaje)
            if not valor.strip():
                raise ValueError("No se permite entrada vacía")

            flotante = float(valor)

            if flotante < minimo:
                raise ValueError(f"El valor debe ser mayor o igual a {minimo}")
            if maximo is not None and flotante > maximo:
                raise ValueError(f"El valor debe ser menor o igual a {maximo}")

            return flotante
        except ValueError:
                print(f"Error: Debes introducir un número (puede ser decimal). Inténtalo de nuevo.")



"""
Muestra las opciones de un Enum y pide al usuario que elija.
Devuelve el valor del Enum seleccionado.
"""
def pedir_enum(mensaje, enum):
    # Obtener lista de opciones
    opciones = list(enum)

    while True:
        try:
            print(f"\n{mensaje}")
            for i, opcion in enumerate(opciones, 1):
                print(f"  {i}. {opcion.value}")

            eleccion = pedir_entero("Elige una opción (número): ", minimo=1, maximo=len(opciones))

            return opciones[eleccion - 1]
        except ValueError as e:
            print(f"Error: {e}")


""" Pregunta sí/no al usuario. Devuelve True para sí, False para no. """
def pedir_si_no(mensaje):
    while True:
        try:
            respuesta = input(mensaje + " (s/n): ").strip().lower()
            if respuesta not in ['s', 'n', 'si', 'no']:
                raise ValueError("Responde 's' o 'n'")
            return respuesta in ['s', 'si']
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
