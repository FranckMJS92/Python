import Utilidades
import random

wins = 0
winUser = 0
winMachine = 0
while wins < 3:
    print("\n========= JUEGO PIEDRA PAPEL O TIJERA =========")
    # Introduce el usuario su opcion
    userOption = Utilidades.pedir_entero_rango(
        "Introduce tu jugada (1-Piedra | 2-PApel | 3-Tijera) : "
    )

    # Se genera la opcion de la maquina
    machineOption = random.randint(1, 3)

    # Variables para guardar las opciones
    gameUser = Utilidades.game(userOption)
    gameMachine = Utilidades.game(machineOption)

    print(f"Tu jugada : {gameUser}")
    print(f"Jugada de la máquina : {gameMachine}")

    # Variable result almacena: string -> mensaje de cada ronda | int -> para evaluar las wins totales
    result = Utilidades.resultString(userOption, machineOption)
    print(f"Resultado : {result[0]}")

    # Logica para sumar las wins de cada partida
    # Los empates no suman por lo que de haber empates se sigue jugando hasta que hayan 3 victorias indistintamente del jugador
    match result[1]:
        case 0:
            winMachine += 1
            # break
        case 1:
            wins += 0
            # break
        case 2:
            winUser += 1
            # break

    wins = winUser + winMachine

print("\n=========================================")
if winUser < winMachine:
    print(f"La maquina gana la partida final : {winUser} - {winMachine}")
else:
    print(f"Has ganado la partida final : {winUser} - {winMachine}")
print("=========================================")
