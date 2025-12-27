import Utilidades

count = 0
while count < 3:
    print("========= JUEGO PIEDRA PAPEL O TIJERA =========")
    workers = Utilidades.pedir_entero(
        "Introduce tu jugada (1-Piedra | 2-PApel | 3-Tijera) : "
    )
    count += 1
