import random

# equivalente a funcion dibujar coche
def draw_car(distancia, pos_a, pos_b):
    """Muestra el estado actual de la carrera"""
    print("\n" + "=" * (distancia + 10))
    print("🎌 CARRERA DE COCHES 🎌")
    print("=" * (distancia + 10) + "\n")

    # Mostrar meta
    print("🏁 META: " + " " * (distancia - 6) + "|FIN|\n")

    # Mostrar pista del coche A (Jugador)
    pista_a = " " * pos_a + "🚗 A" + " " * (distancia - pos_a)
    print(f"Jugador:  |{pista_a}|🏁 ({pos_a}/{distancia})")

    # Mostrar pista del coche B (Máquina)
    pista_b = " " * pos_b + "🚙 B" + " " * (distancia - pos_b)
    print(f"Máquina:  |{pista_b}|🏁 ({pos_b}/{distancia})")

    # Línea de meta visual
    print("\n" + "-" * (distancia + 10))


# Determina la ocurrencia de los eventos
def determinate_event():
    numero = random.random()  # Número entre 0.0 y 1.0

    if numero < 0.2:  # 20% de probabilidad
        return "pinchazo", -5  # Retrocede 5
    elif numero < 0.5:  # 30% de probabilidad (0.2 a 0.5)
        return "turno_bueno", 5  # Avanza 5
    else:  # 50% de probabilidad (0.5 a 1.0)
        return "nada", 0  # No avanza


def show_event(evento, nombre_coche):
    """Muestra el mensaje correspondiente al evento"""
    mensajes = {
        "pinchazo": f"💥 ¡{nombre_coche} PINCHÓ! Retrocede 5 casillas",
        "turno_bueno": f"✨ ¡{nombre_coche} TURNO BUENO! Avanza 5 casillas",
        "nada": f"➖ {nombre_coche} no avanza este turno",
    }
    print(mensajes[evento])


def go_car(pos_actual, distancia, nombre_coche):
    evento, avance = determinate_event()
    nueva_pos = pos_actual + avance

    # No puede ser menor que 0
    if nueva_pos < 0:
        nueva_pos = 0

    # No puede pasar la meta
    if nueva_pos > distancia:
        nueva_pos = distancia

    return nueva_pos, evento, avance
