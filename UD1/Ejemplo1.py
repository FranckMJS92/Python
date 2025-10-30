edad  = int(input("Dime tu edad"))
nombre = "franck"
apellid="Lopez"

#print(f" ... ") <- Facilita la concatenacion de variables y texto en el print
print(f"Tu nombre {nombre}  {apellid} y tienes {edad}")

#Metodo de String
print(nombre.capitalize())

#Condiconal no necesita parentesis ni llaves, para else-if se abrevia "elif"
if edad < 18:
    print("Es menor de edad")
elif edad > 65:
        print("Es jubilado")

#Bucles

"""While
opcion = 0

while opcion<5:
    print("1. Option one")
    print("2. Option two")
    print("3. Option three")
    print("4. Option four")
    print("5. Option five")"""

"""For"""

for _ in range(5):
    print("Hola")