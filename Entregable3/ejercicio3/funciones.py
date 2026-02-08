# Funciones
def ordernar_lista(lista):

    # tamaño de la lista
    n = len(lista)

    # Copia superficial de lista original
    nueva_lista = lista.copy()

    # Como range no toma en cuenta el ultimo valor
    # Para que evalue hasta la  penultima posicion seria n-1 (bucle "i" )
    for i in range(n-1):
        # El indice con el menor numero es el indicado de la iteracion
        min_id=i
        # Para comparar el indice "i" con el siguiente de la lista debe inicar en i+1
        # Termina en "n" para que considere hasta el,ultimo elemento de la lista
        for j in range(i+1,n):
            # Se actualiza min_id si el numero en j es mayor que en i
            # min_id eta asignado a i para iterar
            if nueva_lista[j]<nueva_lista[min_id]:
                min_id = j
        # Intercambia posiciones en la lista
        nueva_lista[i], nueva_lista[min_id] = nueva_lista[min_id], nueva_lista[i]

    return nueva_lista

def busqueda_binaria(lista, elemento, inicio=0, fin):
    return 0
