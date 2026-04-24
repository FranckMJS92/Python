from UD_6_Ejemplo_MVC.Controllers.ProductoController import ProductoController

controlador = ProductoController()

while True:
    controlador.mostrar_menu()

    opcion = input("Escribe una opcion: ")

    match opcion:
        case "1":
            controlador.mostrar_productos()
        case "2":
            categoria = input("Escribe una categoria: ")
            controlador.mostrar_categorias(categoria)
        case "3":
            nombre = input("Escribe una nombre: ")
            categoria = input("Escribe una categoria: ")
            precio = input("Escribe una precio: ")
            stock = input("Escribe una stock: ")
            controlador.insertar_producto(nombre, categoria, precio, stock)
        case "4":
            id = input("Escribe una id del producto: ")
            controlador.eliminar_producto(id)
        case "5":
            break
        case _:
            print("Opcion invalida")
