# Definimos la lista de nombres vacia
nombres = []

while True:
    nombre = input("Ingrese el nombre del conductor: ")
    # Condicion de salida
    if nombre.upper() == "FIN":
        break

    nombres .append(nombre)

# Recorremos la lista de nombres y lo añadimos en el fichero
with open("nombres.txt", "w", encoding="utf-8") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
