class AnimalView:
    """
    Vista para la gestión de animales.
    Se encarga de toda la interacción con el usuario (entrada/salida de datos).
    No contiene lógica de negocio, solo presentación.
    """

    def mostrar_animales(self, animales):
        """
        Muestra los animales en formato tabla con columnas alineadas.
        Args:
            animales (list[Animal]): Lista de objetos Animal a mostrar
        """
        # Cabecera formateada
        print("\n" + "-" * 70)
        print(f"{'ID':<4} | {'Nombre':<15} | {'Especie':<10} | {'Edad':<5} | {'Adoptado':<8}")
        print("-" * 70)
        # Filas de datos
        for a in animales:
            print(f"{a.id:<4} | {a.nombre:<15} | {a.especie:<10} | {a.edad:<5} | {a.adoptado:<8}")

        print("-" * 70)

    def mostrar_menu(self):
        """
        Muestra el menú principal de opciones del programa.
        Incluye iconos emoji para mejorar la experiencia visual.
        """
        print("*" * 15 + " MENU " + "*" * 15)
        print("1. Listar todos los animales 🐦‍🔥")
        print("2. Buscar animales por especie 🐶")
        print("3. Agregar un nuevo animal ✅")
        print("4. Adoptar un animal 🐕‍🦺")
        print("5. Eliminar un animal ❌")
        print("6. Guardar animales en un archivo CSV 🧾")
        print("7. Salir 👋")
        print("*" * 36)

    def mostrar_mensaje(self, mensaje):
        """
        Muestra un mensaje genérico al usuario.
        Args:
            mensaje (str): Texto del mensaje a mostrar
        """
        print(mensaje)
