def invertir_cadena(cadena):
    # CASO BASE: Si la cadena tiene longitud 0 o 1
    # Se devuelve la misma cadena porque no hay que invertir
    if len(cadena) == 0 or len(cadena) == 1:
        return cadena

    letra=cadena[0]
    cadena = cadena[1:len(cadena)]

    return invertir_cadena(cadena) + letra

palabra = input("Ingrese una palabra para invertirla: ")

print(f'Cadena Inveertida : {invertir_cadena(palabra)}')