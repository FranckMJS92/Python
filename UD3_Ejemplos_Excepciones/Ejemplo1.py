# DIVSION POR CERO
edad = 18
try:
    print(edad / 0)

except ZeroDivisionError:
    print("La division no es valida!")

# VALOR INCORRECTO INGRESADO
while True:
    try:
        precio = int(input("Ingrese precio:"))
        break
    except ValueError:
        print("Valor incorrecto")


# PROPAGACION DE EXCEPCIONES -> RAISE
def divisin(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisor no puede ser zero")


# Para ver el mensaje del error hay que importar sys -> import sys
# print(sys.exc_info)
# tipo, valor, traza = sys.exc_info()

# ASSERT
# AssertionError -> Se puede capturar y tratar
try:
    a = 3
    b = 0
    assert b != 0
    print(a / b)
except AssertionError:
    print("No se cumple assert")


# COMPROBACION DE TIPO
x = 3
if type(x) != int:
    raise TypeError("i debe ser numerico")
