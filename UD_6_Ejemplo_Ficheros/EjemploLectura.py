# Esccribimos en el fichero
with open("notas.txt", "w+") as f:
    f.write("Ana,5\n")
    f.write("Luis,4\n")

# Leemos todo el contenido
print("LECTURA CON READ")
print("="*18)
f = open("notas.txt", "r")
contenido = f.read()
print(contenido)
f.close()

print("\nLECTURA CON READ CON WITH")
print("="*28)
with open("notas.txt", "r", encoding="utf-8") as f:
    for line in f:
        nombre, nota = line.strip().split(",")
        if int(nota) >= 5:
            print(nombre,"Ha aprobado")