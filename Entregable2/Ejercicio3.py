import Utilidades
import GestionCarrera

# Inicio del programa
print("=" * 50)
print("        🏁 CARRERA DE COCHES 🏁")
print("=" * 50)

# Mostrar probabilidades
print("\n📊 PROBABILIDADES DE EVENTOS:")
print("   💥 Pinchazo: 20% -> Retrocede 5 casillas")
print("   ✨ Turno bueno: 30% -> Avanza 5 casillas")
print("   ➖ Nada: 50% -> No avanza")
print("-" * 40)

# Pedir y validar distancia
distance_input = Utilidades.pedir_entero_rango(
    "\nIntroduce la distancia de la carrera (30-60): ", 30, 60
)

# Inicializar posiciones
pos_a = 0  # Coche jugador
pos_b = 0  # Coche máquina
turno = 1

print("\n" + "=" * 50)
print("¡PREPARADOS! Presiona ENTER para cada turno.")
print("=" * 50)

# Bucle principal del juego
while pos_a < distance_input and pos_b < distance_input:
    input(f"\n🎮 Turno {turno} - Presiona ENTER para avanzar...")
    Utilidades.limpiar_pantalla()

    # Turno del jugador (Coche A)
    print("\n🎮 TURNO DEL JUGADOR 🎮")
    pos_a, evento_a, avance_a = GestionCarrera.go_car(pos_a, distance_input)
    GestionCarrera.show_event(evento_a, "Jugador")

    # Turno de la máquina (Coche B)
    print("\n🤖 TURNO DE LA MÁQUINA 🤖")
    pos_b, evento_b, avance_b = GestionCarrera.go_car(pos_b, distance_input)
    GestionCarrera.show_event(evento_b, "Maquina")

    # Mostrar estado actual
    GestionCarrera.draw_car(distance_input, pos_a, pos_b)

    # Resumen del turno
    print(f"\n📝 RESUMEN TURNO {turno}:")
    print(f"   🚗 Jugador: {evento_a.title()} (avance: {avance_a:+})")
    print(f"   🚙 Máquina: {evento_b.title()} (avance: {avance_b:+})")

    # Verificar si alguien ganó
    if pos_a >= distance_input and pos_b >= distance_input:
        print("\n" + "=" * 50)
        print("🏆 ¡EMPATE! Ambos llegaron a la vez 🏆")
        print("=" * 50)
        break
    elif pos_a >= distance_input:
        print("\n" + "=" * 50)
        print("🏆 ¡FELICIDADES! ¡GANASTE! 🏆")
        print("=" * 50)
        break
    elif pos_b >= distance_input:
        print("\n" + "=" * 50)
        print("😞 ¡PERDISTE! La máquina ganó 😞")
        print("=" * 50)
        break

    turno += 1

# Estadísticas finales
print(f"\n📊 RESUMEN DE LA CARRERA:")
print(f"   Distancia total: {distance_input} casillas")
print(f"   Turnos jugados: {turno}")
print(f"   Posición final Jugador: {pos_a}/{distance_input}")
print(f"   Posición final Máquina: {pos_b}/{distance_input}")

input("\nPresiona ENTER para salir...")
