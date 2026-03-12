import pickle
from pathlib import Path

alumnos = {}

while True:
    nombre = input("Ingrese un nombre: ")
    if nombre.upper() == "FIN":
        break

    notas_entrada = input("Ingrese un notas(separadas por comas): ")
    notas = [float(n.strip()) for n in notas_entrada.split(",") ]

    alumnos[nombre] = notas

archivo = Path("alumnos.pkl")
with archivo.open("wb") as f:
    pickle.dump(alumnos, f)