import Utilidades

# Parte1 : Peticion al usuario para que ingrese los datos necesarios para el programa

print("=========== DATOS PARA CALIFICACION DEL CENTRO ===========")

workers = Utilidades.pedir_entero("Número total de trabajadores : ")

distance = Utilidades.pedir_float("Distancia al centro de la ciudad (km) : ")

price = Utilidades.pedir_float("Precio alquiler mensual por sala : ")

discount = Utilidades.pedir_float(
    "Porcentaje de descuento sobre el precio del alquiler mensual : "
)

restRoom = Utilidades.pedir_entero_rango(
    "¿Tiene sala de descanso? (Si = 1 / No = 0) : "
)

# Part2: Calculos adicionales

qtyRooms = Utilidades.redondear_salas(workers)

totalPrice = price * qtyRooms * (1 - discount / 100)  # Calculo del precio final
totalPrice = Utilidades.redondear(totalPrice)  # Asignacion del redondeo del precio final

# Variable calification y logica condicional para asignar el valor correspondiente
calification = ""
if qtyRooms <= 1:
    calification = "Pequeño"
elif 2 <= qtyRooms <= 3:
    calification = "Mediano"
else:
    calification = "Grande"


# Part3: Logica condicional para determinar la idoneidad del centro
status = (
    "CENTRO IDONEO"
    if distance < 5 and price <= 100 and restRoom == 1
    else "CENTRO NO IDONEO"
)

# Part4: Mostrar en pantalla datos almacenados y calculados
print("\n======= DATOS INGRESADOs =======")
print(f"Numero Trabajadores : {workers}")
print(f"Distancia al centro (km) : {distance} km")
print(f"Precio alquiler por sala : {price} €")
print(f"Descuento sobre el precio : {discount} %")
print(f"Sala de descanso : {"SI" if restRoom==1 else "NO"}")

print("\n======= DATOS CALCULADOS =======")
print(f"Salas Necesarias : {qtyRooms}")
print(f"Precio Final del Alquiler : {totalPrice} €")
print(f"Calificacion del Centro : {calification}")
print(f"Calificacion del centro : {status}")
