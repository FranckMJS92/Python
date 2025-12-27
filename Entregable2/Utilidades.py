import math

# ARCHIVO DE UTILIDADES PARA EJERCICIOS 1 Y 2

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("El valor no es entero")


def pedir_entero_rango(mensaje, min=0, max=1):
    while True:
        try:
            valor = int(input(mensaje))
            if max >= valor >= min:
                return valor
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except ValueError:
            print("El valor no es entero")

def redondear(numero):
    return round(numero, 2)