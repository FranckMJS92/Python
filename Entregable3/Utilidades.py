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
