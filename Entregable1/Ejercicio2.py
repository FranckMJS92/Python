import Utilidades

# Parte1 : Peticion al usuario para que ingrese los datos necesarios para el programa

print("=========== DATOS PARA EL CALCULO DE COSTO DE MENSAJERIA ===========")

weight = Utilidades.pedir_float("Peso del paquete (kg) : ")

distance = Utilidades.pedir_float("Distancia a recorrer (km) : ")

price = Utilidades.pedir_float("Precio base por kilogramo (€) : ")

extra = Utilidades.pedir_float("Suplemento por envio urgente (€) : ")

protection = Utilidades.pedir_entero_rango(
    "¿Incluye seguro adicional? (Si = 1 / No = 0) : "
)

# Part2: Calculos

# Calculo del coste de envio
shippingCost = weight * price
shippingCost = Utilidades.redondear(shippingCost)

# El costo con suplemento es el primer costo calculado para el extra ingresado de ser el caso
costSuplement = shippingCost + extra
costSuplement = Utilidades.redondear(costSuplement)

# Calculo del costo final aumento el porcentaje del seguro de ser el caso
finalCost = costSuplement if protection == 0 else costSuplement * 1.08
finalCost = Utilidades.redondear(finalCost)

# Variable calification y logica condicional para asignar el valor correspondiente
calification = ""
if weight <= 2:
    if distance <= 30:
        calification = "Rapido"
    else:
        calification = "Normal"
else:
    calification = "Especial"


# Part3: Logica condicional para determinar calificacion economica del envio
status = "Economico" if finalCost < 20 and distance < 30 and weight < 2 else "Costoso"

# Part4: Mostrar en pantalla datos almacenados y calculados

print("\n======= DATOS INGRESADOs =======")
print(f"Peso del Paquete : {weight} KG")
print(f"Distancia a recorrer : {distance} KM")
print(f"Precio base por kg : {price} €")
print(f"Suplemento Urgente : {extra} €")
print(f"Seguro Adicional : {"SI" if protection==1 else "NO"}")

print("\n======= DATOS CALCULADOS =======")
print(f"Costo de Envio : {shippingCost} €")
print(f"Costo con suplemento de urgencia (si corresponde) : {costSuplement} €")
print(f"Costo Final Evio : {finalCost} €")
print(f"Calificacion del Envio : {calification}")
print(f"Envio : {status}")
