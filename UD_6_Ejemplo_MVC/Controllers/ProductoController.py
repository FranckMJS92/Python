from UD_6_Ejemplo_MVC.Views.ProductoView import ProductoView
from UD_6_Ejemplo_MVC.Models.ProductoModel import ProductoModel


class ProductoController:

    def __init__(self):
        self.modelo = ProductoModel()
        self.vista = ProductoView()

    def mostrar_productos(self):
        productos = self.modelo.listar_productos()
        self.vista.mostrar_productos(productos)

    def mostrar_categorias(self, categoria):
        productos = self.modelo.listar_categorias(categoria)
        self.vista.mostrar_mensaje("Productos por categoria")
        self.vista.mostrar_productos(productos)

    def insertar_producto(self, nombre, categoria, precio, stock):
        id = self.modelo.insertar_producto(nombre, categoria, precio, stock)
        if id is not None:
            self.vista.mostrar_mensaje("Producto insertado correctamente")
        else:
            self.vista.mostrar_mensaje("Error al insertar el producto")

    def eliminar_producto(self, id):
        count = self.modelo.eliminar_producto(id)
        if count > 0:
            self.vista.mostrar_mensaje("Producto eliminado correctamente")
        else:
            self.vista.mostrar_mensaje("Error al eliminar producto")

    def mostrar_menu(self):
        self.vista.mostrar_menu()