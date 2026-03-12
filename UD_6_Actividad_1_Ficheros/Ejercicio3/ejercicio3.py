import csv
from pathlib import Path

archivo = Path("alumnos.csv")

# Comporbamos si existe
existe = archivo.exists()

with archivo.open("a", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f,delimiter=",")


    # Escribimos la cabecera si no existe el fichero
    if not existe:
        escritor.writerow(["nombre","edad","curso","nota"])

    # Bucle para pedir datos
    while True:
        nombre = input("Nombre (FIN para terminar): ")
        if nombre.upper() == "FIN":
            break
        edad = input("Edad: ")
        curso =  input("Curso: ")
        nota = input("Nota: ")

        escritor.writerow([nombre,edad,curso,nota])
