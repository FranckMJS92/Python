"""
Módulo de utilidades para validación de entrada de datos.
Contiene funciones reutilizables para solicitar y validar datos al usuario.
"""

def pedir_cadena(mensaje):
    """
    Pide una cadena al usuario.
    No permite cadenas vacías o solo espacios.
    Devuelve la cadena en formato título: Primera letra de cada palabra en mayúscula.
    Args:
        mensaje (str): Mensaje que se muestra al usuario
    Returns:
        str: Cadena validada en formato título (ej: "Juan Perez")
    """
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                raise ValueError("La entrada no puede estar vacía")
            return valor.lower().title()  # Convierte a minúsculas y luego capitaliza
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")


def pedir_entero_rango(mensaje, min=0, max=25):
    """
    Solicita la entrada de un número entero dentro del rango indicado.
    Args:
        mensaje (str): Mensaje que se muestra al usuario
        min (int): Valor mínimo permitido (por defecto 0)
        max (int): Valor máximo permitido (por defecto 25)
    Returns:
        int: Número entero validado dentro del rango
    Example:
        >>> pedir_entero_rango("Edad: ", 0, 120)
    """
    while True:
        try:
            valor = int(input(mensaje))
            if max >= valor >= min:
                return valor
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except ValueError:
            print("El valor no es un número válido")


def pedir_si_no(mensaje):
    """
    Pregunta sí/no al usuario.
    Args:
        mensaje (str): Mensaje que se muestra al usuario
    Returns:
        int: 1 para sí (True), 0 para no (False)
    Example:
        >>> adoptado = pedir_si_no("¿Está adoptado?")
        >>> if adoptado:
        ...     print("El animal ha sido adoptado")
    """
    while True:
        try:
            respuesta = input(mensaje + " (s/n): ").strip().lower()
            if respuesta not in ['s', 'n', 'si', 'no']:
                raise ValueError("Responde 's' o 'n'")
            return 1 if respuesta in ['s', 'si'] else 0
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
