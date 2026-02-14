from Entregable3.ejercicio1.textos import *

print("="*8 + " INICIO DEL PROGRAMA " + "="*8)

while(True):
    cadena = input("Introduce una frase (vacía para terminar): ")

    # Condicional para salir del bucle en caso la cadena ingresada por usuario sea vacia
    if cadena == "":
        print("="*8 + " FIN DEL PROGRAMA " + "="*8)
        break

    print(depurar_cadena(cadena))

    if(len(depurar_cadena(cadena))<1):
        break
    # Ejecuta e imprime resultado de los metodos siempre que la cadena no esté vacía
    print(f'Número de palabras : {contar_palabras(cadena)}')
    print(f'Número total de caracteres (sin espacios ni puntuación): {caracteres_total(cadena)}')
    print(f'Palabra mas larga: {palabra_mas_larga(cadena)}')

print("="*8 + " PROGRAMA TERMINADO " + "="*8)


