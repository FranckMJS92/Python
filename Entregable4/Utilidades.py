import os

def depurar_cadena(cadena):
    # Tupla de signos para saber que signos atacar
    signos = (",", ".", ";", ":", "!", "¡", "?", "¿", " ")
    # Recorrido de cadena y reemplazo todos los signos por espacios
    for caracter in signos:
        cadena = cadena.replace(caracter, " ")

    # Metodo strip() de string
    # Elimina espacios en blanco al principio y/o final
    cadena = cadena.strip()
    return cadena

def validar_cadena_depurada(cadena):
    if(len(depurar_cadena(cadena))<1):
        return False
    else:
        return True

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

# Limpia la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')