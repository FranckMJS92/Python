import Utilidades
import GestionCuenta

print("\n============ DATOS BANCARIOS ============")
# Saldo Inicial
initialMount = Utilidades.pedir_float("Ingrese el saldo inicial de la cuenta : ")
# Saldo corriente
currentMount = 0 + initialMount
# Contaddores ingresos y retiros
numDeposit = 0
numWithdraw = 0

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
            numDeposit += 1
        case 2:
            currentMount -= GestionCuenta.withdraw(currentMount)
            numWithdraw += 1
        case 3:
            GestionCuenta.show(currentMount, initialMount)
        case 4:
            GestionCuenta.statistics(numDeposit, numWithdraw)
        case 5:
            break

print("Muchas gracias, hasta luego!")
