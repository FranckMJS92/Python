import Utilidades
import GestionCuenta

currentMount = 0

print("\n============ DATOS BANCARIOS ============")
initialMount = Utilidades.pedir_float("Ingrese el saldo inicial de la cuenta : ")
currentMount += initialMount

while True:
    print("\n============ MENU OPCIONES ============")
    print("1.- Ingresar dinero")
    print("2.- Retirar dinero")
    print("3.- Mostrar saldo")
    print("4.- Estadisticas")
    print("5.- Salir")

    option = Utilidades.pedir_entero_rango("Elija la opcion deseada por favor : ", 1, 5)

    match option:
        case 1:
            currentMount += GestionCuenta.deposit()
        case 2:
            currentMount -= GestionCuenta.withdraw(currentMount)
        case 3:
            GestionCuenta.show(currentMount, initialMount)
        case 4:
            GestionCuenta.statistics()
        case 5:
            break
