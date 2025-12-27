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


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("valor no valido")


# Se toma el numero de trabajadores / 10
# ya que es el maximo de capacidad de 1 sala
# y se redondeo al numero superior para determinar las salas necesarias
def redondear_salas(numero):
    return math.ceil(numero / 10)


def redondear(numero):
    return round(numero, 2)
