def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("El valor ingresado no es un numero")

valor1 = pedir_entero("Dime tu edad: ")
