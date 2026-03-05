from pathlib import Path

dias = ["Lunes", "MArtes" , "Miercoles" , "Jueves" , "Viernes" , "Sabado" , "Domingo"]

temperaturas = []

for dia in dias:
    temp = float(input(f"Temperatura de la {dia} : "))
    temperaturas.append(temp)

with open ("temperaturas.txt", "w", encoding="utf-8") as archivo:
    for dia, temp  in zip(dias, temperaturas):
        archivo.write(f"{dia} : {temp}\n")


# LECTURA DEL ARCHIVO

archivo = Path("temperaturas.txt")
contador = 0
totalTemperaturas = 0
if archivo.exists():
    with open("temperaturas.txt", "r", encoding="utf-8") as archivo:
        for line in archivo:
            print(line, end='')
            # Separa cada linea por:
            partes = line.strip().split(":")
            temp =  float(partes[1])
            totalTemperaturas += temp
            contador += 1

print(f"Total de temperaturas: {totalTemperaturas}")
print(f"Media de temperaturas: {totalTemperaturas/contador}")
print(f"Maxima temperatura: {max(temperaturas)}")