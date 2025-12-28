import Utilidades

def deposit():
    print("\n============ INGRESO EN CUENTA ============")
    sumMount = Utilidades.pedir_float(
        "Ingrese la cantidad que desea ingresar a su cuenta : "
    )
    return sumMount

def withdraw(currentMount):
    print("\n============ RETIRO DE CUENTA ============")
    lessMount = Utilidades.pedir_float(
        "Ingrese la cantidad que desea retirar de su cuenta : "
    )
    if lessMount > currentMount:
        print("Retiro no puede exceder el saldo bancario actual")
    else:
        return lessMount

def show(currentMount, initialMount):
    print("\n====== SALDO DE LA CUENTA =====")
    print(f"Saldo Inicial : {initialMount} €")
    print(f"Saldo Actual : {currentMount} €")

def statistics(numDeposit, numWithdraw):
    print("\n============ ESTADISTICAS ============")
    print(f"Numeros de Ingresos : {Utilidades.redondear(numDeposit)}")
    print(f"Numeros de Retiros : {Utilidades.redondear(numWithdraw)}")
