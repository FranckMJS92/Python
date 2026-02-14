from Entregable3.Utilidades import validar_cadena_depurada
from Entregable3.ejercicio1.textos import *

print("="*8 + " INICIO DEL PROGRAMA " + "="*8)

while(True):
    cadena = input("Introduce una frase (vacía para terminar): ")

    # Condicional para salir del bucle en caso la cadena ingresada por usuario sea vacia
    if cadena == "":
        break

    cadena_depurada = depurar_cadena(cadena)

    if(not validar_cadena_depurada(cadena_depurada)):
        break

    print(f'Cadena Depurada : {cadena_depurada}')

    # Ejecuta e imprime resultado de los metodos siempre que la cadena no esté vacía
    print(f'Número de palabras : {contar_palabras(cadena)}')
    print(f'Número total de caracteres (sin espacios ni puntuación): {caracteres_total(cadena)}')
    print(f'Palabra mas larga: {palabra_mas_larga(cadena)}')

print("="*8 + " PROGRAMA TERMINADO " + "="*8)


