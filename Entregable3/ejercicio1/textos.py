from Entregable3.Utilidades import depurar_cadena


def contar_palabras(cadena):
    cadena_depurada = depurar_cadena(cadena)

    #Separo las palabras en un array
    array_cadena = cadena_depurada.split()

    # Devuelvo la longitud del array que seria el total de palabras
    return len(array_cadena)

def caracteres_total(cadena):
    cadena_depurada = depurar_cadena(cadena)
    contador = 0

    # Recorro la cadena depurada la cual no tiene espacios
    # cada iteracion aumenta el contador que seria el numero de caracteres
    for caracter in cadena_depurada.replace(' ',''):
        contador+=1
    return contador

def palabra_mas_larga(cadena):
    cadena_depurada = depurar_cadena(cadena)

    # Separo las palabras en un array
    array_cadena = cadena_depurada.split()

    # Declara variable para return
    valor = array_cadena[0]

    # Recorre el array y almacen la palabra en variable 'valor'
    # Luego compara longitudes y reasigna
    for i in range(len(array_cadena)-1):
        if len(valor) < len(array_cadena[i+1]):
            valor = array_cadena[i+1]
    return valor
