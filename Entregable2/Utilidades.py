import os

# Valida la opcion ingresada por usuario en el rango
def pedir_entero_rango(mensaje, min=1, max=3):
    while True:
        try:
            valor = int(input(mensaje))
            if max >= valor >= min:
                return valor
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except ValueError:
            print("El valor no es entero")


# Define la interpretacion de la opcion ingresada por el usuario
def game(numero):
    match numero:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"


# Valida el resultado y devuelve un String y un entero
# El string se muestra directo en el resultado de cada ronda
# El entero sirve para evaluar la cantidad de victorias y mostrar el resultado final
def resultString(n1, n2):
    if n1 < n2:
        return "Pierdes esta ronda ... ", 0
    elif n1 == n2:
        return "Empates ...", 1
    elif n1 > n2:
        return "¡Ganas esta ronda!", 2


# Validacion de numero decimal mayor que cero ingresado por usuario
def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Valor debe ser un numero mayor que cero")
            else:
                return redondear(valor)
        except ValueError:
            print("valor no valido")


# Redondeo para calculo de float
def redondear(numero):
    return round(numero, 2)


def validateDistance(distance):
    "Valida que la distancia esté entre 30 y 60"
    try:
        distance_int = int(distance)
        if 30 <= distance_int <= 60:
            return distance_int, True
        else:
            return None, False
    except ValueError:
        return None, False

def limpiar_pantalla():
    "Limpia la pantalla según el sistema operativo"
    os.system('cls' if os.name == 'nt' else 'clear')