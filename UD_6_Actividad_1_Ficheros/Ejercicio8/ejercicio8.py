import pickle
from pathlib import Path

class Producto:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad} - Categoria: {self.categoria}"


#lista para guardar los productos
inventario = []

# PARTE 1 : Si el archivo existe, cargamos los productos que hay guardados
archivo = Path("inventario.pkl")
if archivo.exists():
    with archivo.open("rb") as f:
        inventario = pickle.load(f)
        print("Cargados los productos del archivo")

else:
    print("No existe el archivo")

# PARTE 2 - Anadir productos
while True:
    nombre = input("Ingrese el nombre del producto(FIN para terminar): ")
    if nombre.upper() == "FIN":
        break;
    # Si no escrcibimos FIN pedimos el resto de los datos
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    categoria = input("Ingrese la categoria del producto: ")

    # Creamos el objeto Producto
    nuevoProducto = Producto(nombre, precio, cantidad, categoria)

    # Lo anadimos a la lista
    inventario.append(nuevoProducto)

    # PARTE3 - Guardamos el inventario actualizado
    with archivo.open("wb") as f:
        pickle.dump(inventario, f)
        print("Cargados los productos del archivo")

    # PARTE 4 - Mostramos el inventario completo
    for producto in inventario:
        print(producto)