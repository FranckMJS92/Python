import json
from pathlib import Path

usuarios = []

while True:
    nombre = input("Nombre(FIN para terminar): ")
    if nombre.upper() == "FIN":
        break

    edad = int(input("Edad: "))

    while True:
        activo_entrada = input("Activo(S/N): ")
        if activo_entrada.upper() in ("S","N"):
            activo = activo_entrada == "S"
            break
        else:
            print("Valor incorrecto")

    roles_entrada = input("Roles(separados por comas): ")
    roles = [ rol.strip()  for rol in roles_entrada.split(",") ]

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "activo": activo,
        "roles": roles,
    }

    usuarios.append(usuario)

archivo = Path("usuarios.json")
with archivo.open("w",encoding="utf-8") as archivo:
    json.dump(usuarios, archivo, indent=4)

