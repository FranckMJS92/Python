import csv

total_alumnos = 0
suma_notas = 0.0
mejor_nota = 0.0
mejor_alumno = ""

with open("alumnos.csv","r",encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=',')
    for row in reader:
        nombre = row["nombre"]
        edad = row["edad"]
        curso = row["curos"]
        nota = float(row["nota"])
        print(f"Nombre: {nombre} - Edad: {edad} - Curso: {curso} - Nota: {nota}")

        total_alumnos +=1
        suma_notas += float(nota)

        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = nombre

if total_alumnos > 0:
    print(f"Total de alumnos: {total_alumnos}")
    print(f"Nota media : {suma_notas / total_alumnos}:.2f")
    print(f"Mejor alumno : {mejor_alumno} - {mejor_nota}")