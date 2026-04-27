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
            return valor.lower().title()
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")


'''
Solicita la entrada de un numero entero en el rango indicado
'''


def pedir_entero_rango(mensaje, min=0, max=25):
    while True:
        try:
            valor = int(input(mensaje))
            if max >= valor >= min:
                return valor
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except ValueError:
            print("El valor no es numero valido")


""" Pregunta sí/no al usuario. Devuelve True para sí, False para no. """


def pedir_si_no(mensaje):
    while True:
        try:
            respuesta = input(mensaje + " (s/n): ").strip().lower()
            if respuesta not in ['s', 'n', 'si', 'no']:
                raise ValueError("Responde 's' o 'n'")
            return 1 if respuesta in ['s', 'si'] else 0
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
