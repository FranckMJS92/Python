import math

# Valida la opcion ingresada por usuario en el rango de 1 a 3
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
        return "Pierdes esta ronda ... ",0
    elif n1 == n2:
        return "Empates ...",1
    elif n1 > n2:
        return "¡Ganas esta ronda!",2
