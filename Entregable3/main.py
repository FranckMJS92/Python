from Entregable3.textos import *

print("="*8 + " INICIO DEL PROGRAMA " + "="*8)

while(True):
    cadena = input("Introduce una frase (vacía para terminar): ")

    # Condicional para salir del bucle en caso la cadena ingresada por usuario sea vacia
    if cadena == "":
        print("="*8 + " FIN DEL PROGRAMA " + "="*8)
        break

    # Ejecuta e imprime resultado de los metodos siempre que la cadena no esté vacía
    print("Número de palabras : " + contar_palabras(cadena))
    print("Número total de caracteres (sin espacios ni puntuación): " + caracteres_total(cadena))
    print("Palabra mas larga: " + palabra_mas_larga(cadena))


