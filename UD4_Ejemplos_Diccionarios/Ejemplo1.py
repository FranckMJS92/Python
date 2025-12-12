notas = {"Juan": 7, "Ana": 8, "Pepe": 9}
notas["Victor"] = 10  # Añadimos elemento

if "Ana" in notas:
    notas["Ana"] = 9  # Modificamos valor
else:
    print("No existe")

print(notas)

# Solo mostrar claves
print("SOLO CLAVES")
for clave in notas.keys():
    print(clave)

# Solo mostrar valores
print("SOLO VALORES")
for value in notas.values():
    print(value)

# Recorremos claves y valores
print("MOSTTAR CLAVE Y VALORES")
for clave, valor in notas.items():
    print(f'{clave:<10}{valor:<10pp´l´kpkoñlñjñlñmlñmlñjmljmlloooooooo||    }')