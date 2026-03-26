from UD_6_Ejemplo_MVC.Models.Producto import Producto
from UD_6_Ejemplo_MVC.conexion import crear_conexion


class ProductoModel:

    def listarProductos(self):
        # Obtener la conexion
        conexion = crear_conexion()
        productos = []

        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            for p in cursor.fetchall():
                productos.append(Producto(*p))

        # Cerrar conexion
        conexion.close()
        return productos

    def listar_categorias(self,categoria):
        # Obtener la conexion
        conexion = crear_conexion()
        productos = []

        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE categoria = %s",(categoria,))
            for p in cursor.fetchall():
                productos.append(Producto(*p))

        # Cerrar conexion
        conexion.close()
        return productos

    def insertar_producto(self,nombre,categoria,precio,stock):
        # Obtener la conexion
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sqlInsert = "INSERT INTO productos (nombre,categoria,precio,stock)  VALUES (%s,%s,%s,%s)"
            valores = (nombre,categoria,precio,stock)
            cursor.execute(sqlInsert, valores)
            conexion.commit()
            cursor.close()
            return cursor.lastrowid
        else:
            return None
