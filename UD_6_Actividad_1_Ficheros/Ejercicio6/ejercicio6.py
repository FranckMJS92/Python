import json
from pathlib import Path

archivo = Path("usuarios.json")

with archivo.open("r", encoding="utf-8") as f:
    usuarios = json.load(f)


for user in usuarios:
    nombre = user["nombre"]
    edad = user["edad"]
    activo = user["activo"]
    roles = user["roles"]

    print(f"Nombre: {nombre} - Edad: {edad} - Activo: {activo} - Roles: {roles}")
