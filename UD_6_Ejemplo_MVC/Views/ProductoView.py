class ProductoView:

    def mostrar_productos(self, productos):
        print("ID || Nombre || Categoria || Precio || Stock")
        for p in productos:
            print(p)

    def mostrar_producto(self, producto):
        print("ID || Nombre || Categoria || Precio || Stock")
        for p in producto:
            print(p)

    def mostrar_menu(self):
        print("1. Mostrar productos")
        print("2. Mostrar producto")
        print("3. Insertar producto")
        print("4. Eliminar producto")
        print("5. Salir")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
