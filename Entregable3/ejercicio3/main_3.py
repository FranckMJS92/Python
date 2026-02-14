from Entregable3.Utilidades import pedir_entero
from Entregable3.ejercicio3.funciones import *

# Declaracion funcion ordenar_lista()
mi_lista = [90,1,13,73,54,26,8,10]
# mi_lista=[1,3,5,7,9]
lista_ordenada = ordernar_lista(mi_lista)

print(f' Lista original : {mi_lista}')
print(f' Lista ordenada : {lista_ordenada}')

inicio = 0
fin = len(lista_ordenada)-1

numero_buscar = pedir_entero("\nIngrese un numero entero para buscar : ")

valor_binario = busqueda_binaria(lista_ordenada, numero_buscar,inicio,fin)

print(f'Valor binario : {valor_binario}')