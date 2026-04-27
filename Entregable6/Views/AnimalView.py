class AnimalView:

    def mostrar_animales(self, animales):
        print("\nID || Nombre || Especie || Edad || Adoptado")
        for a in animales:
            print(a)

    def mostrar_menu(self):
        print("*" * 15 + " MENU " + "*" * 15)
        print("1. Listar todos los animales 🐦‍🔥")
        print("2. Buscar animnales por especie 🐶")
        print("3. Agregar un nuevo animal ✅")
        print("4. Adoptar un animal 🐕‍🦺")
        print("5. Eliminar un animal ❌")
        print("6. Guardar animales en un archivo CSV 🧾")
        print("7. Salir 👋")
        print("*" * 36)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
