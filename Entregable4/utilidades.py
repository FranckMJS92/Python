import os

# Pide al usuario la cadena de texto
# Retorna mensaje si la cadena esta vacia y solicita ingreso nuevo
# Si valor es correcto, quita espacios y le da formato como
# se encuentran los titulos en el diccionario
def pedir_texto(mensaje):
    while True:
        valor = input(mensaje)
        if len(valor) > 0:
            valor=valor.strip().lower().title()
            return valor
        else:
            print("No puede ser vacio")


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

def mostrar_menu():
        print("\n============ MENU OPCIONES ============")
        print("1.- Mostrar todos")
        print("2.- Agregar serie/película")
        print("3.- Eliminar serie/película")
        print("4.- Buscar serie/película")
        print("5.- Actualizar valoración")
        print("6.- Filtrar por género")
        print("7.- Mostrar mejores series/peliculas")
        print("8.- Salir")