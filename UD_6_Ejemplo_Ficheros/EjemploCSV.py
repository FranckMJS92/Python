# Importamos la libreria
import csv

with open("datos.csv","w",newline="",encoding="utf-8") as csvfile:
    # Creamos un obvjeto "escritor", indicamos el delimitador
    escritor = csv.writer(csvfile,delimiter=",")
    # Primera fila: cabecera
    escritor.writerow(["nombre","apellido","edad"])
    # Siguientes filas: datos del fichero
    escritor.writerow(["Ana", "Perez",20])
    escritor.writerow(["Pepe", "Gomez",20])

# Leemos el fichero CSV
with open("datos.csv","r",encoding="utf-8") as csvfile:
    # Creamos un obvjeto "lector", indicamos el delimitador
    lector = csv.reader(csvfile,delimiter=",")
    for row in lector:
        print(row)