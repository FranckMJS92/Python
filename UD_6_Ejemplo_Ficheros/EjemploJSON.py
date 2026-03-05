# Importamos la libreria
import json

usuario = [
    {
        "nombre": "Ana",
        "apellido": "Perez",
        "notas": [5,7,8]
    },
    {
        "nombre": "Luis",
        "apellido": "Castillo",
        "notas" : [8,2,3]
    }
]

# Guardamos lña lista de usuarios en el archiuvo JSON
with open("datos.json","w",encoding="utf-8") as jsonfile:
    json.dump(usuario,jsonfile,indent=4)

# Leemos el fichero JSON
with open("datos.json","r",encoding="utf-8") as jsonfile:
    # Load: convertimos una lista de diccionarios
    datos = json.load(jsonfile)

for usuario in datos:
    print(usuario["nombre"])
    for nota in usuario["notas"]:
        print(nota)