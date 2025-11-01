#Introduccion de datos
from operator import truediv

valor = input("Dime un numero : ")
print(type(valor)) #El tipo de la variable introducida es String


valor=int(input("Dime un numero : ")) #Se realiza como un casteo
print(type(valor))

edad  = int(input("Dime tu edad"))
nombre = "franck"
apellido="Lopez"

#print(f" ... ") cadenas f <- Facilita la concatenacion de variables y texto en el print
print(f"Tu nombre {nombre}  {apellido} y tienes {edad}")

#Para que el print no haga salto de linea
print("El numero es:",end=" ")
print(valor)

#Metodo de String
print(nombre.capitalize())

#Subcadena de String
nombre= "Pepe Perez"
nombre1 = nombre[0:4]

#Todo MAYUSCULA MINUSCUla
nombre.upper()
nombre.lower()


#Condicional no necesita parentesis ni llaves, para else-if se abrevia "elif"
opcion = 2
if 1<=opcion<=5:
    print(opcion)


if edad < 18:
    print("Es menor de edad")
elif edad > 65:
        print("Es jubilado")
else:
    print("No es jubilado")


correcto = True

if not correcto:
    print("Error")
else:
    print("Correcto")


#Condicional Switch

menu = input("Dime una opcion")

match menu:
    case "1" | 1:
        print("Opcion 1")
    case "2" | 2:
        print("Opcion 2")
    case "3" | 3:
        print("Opcion 3")
    case _:
        print("Opcion invalida")

#random

import random

ram1 = random.randint(2,8)
print(ram1)

ram2=random.random()*10
print(ram2)

#Bucles

#While
opcion = 0

while opcion!=5:
    print("1. Option one")
    print("2. Option two")
    print("3. Option three")
    print("4. Option four")
    print("5. Option five")
    opcion = int(input("Seleccione una opcion [1-5]: "))

#FOR

#Como un foreach
for x in ["Ana","Pepe","Eva"]:
    print(x)
#Genera 10 numeros del 0 al 9
for x in range(10):
    print(x)
#Empieza por 5
for x in range(5,10):
    print(x)
#Empieza por 5 y va de 2 en dos por el ultimo parametro
for x in range(5,12,2):
    print(x)
#Recorre texto como una lista
for x in "hola mundo":
    print(x)
#Imprime 5 "hola mundo" no se usa variable x entonces se puede poner _
for _ in range(5):
    print("Hola mundo")
#Anidado
for x in range(5):
    for y in range(5):
        print(x,y)