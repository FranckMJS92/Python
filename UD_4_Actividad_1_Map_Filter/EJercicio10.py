# EJERCICIO 10

print("EJERCICIO 10")


# Funcion Menu
def menu():
    # while True:
    print("-" * 8 + "MENU" + "-" * 8)
    print("1. Aplicar el IVA (21%) a todos los productos y mostrar el precio con IVA.")
    print("2. Mostrar los productos con stock bajo (<10 unidades).")
    print("3. Ordenar los productos por precio y, en caso de empate, por nombre.")
    print("4. Salir del programa.")
    input("Dime una opcion : ")


# Funcion Aplicar IVA
def aplicarIVA():
    print(productos.items)
    print(productos.values)
    # precioConIVA= map(lambda item : )


# Diccionario de productos
productos = {
    "123456": {"nombre": "Manzanas", "precio": 1.5, "stock": 20, "categoria": "Fruta"},
    "234567": {"nombre": "Leche", "precio": 0.9, "stock": 5, "categoria": "Lácteo"},
    "345678": {"nombre": "Pan", "precio": 1.0, "stock": 8, "categoria": "Panadería"},
    "456789": {"nombre": "Huevos", "precio": 2.5, "stock": 12, "categoria": "Lácteo"},
    "567890": {"nombre": "Platanos", "precio": 1.8, "stock": 3, "categoria": "Fruta"},
}

menu()
aplicarIVA()
