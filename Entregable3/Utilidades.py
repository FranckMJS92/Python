def validar_input(mensaje):
    while True:
        try:
            valor = str(input(mensaje))
            if isinstance(valor, str):
                return valor
        except ValueError:
            print("El valor no es entero")


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