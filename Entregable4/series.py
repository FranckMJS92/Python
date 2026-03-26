from Entregable4.utilidades import *

def mostrar_todos(catalogo):
    # Si catalogo esta vacio devuelve mensaje
    if len(catalogo) == 0:
        print("No existen peliculas o series")
    else:
        print() # Espacio para mostrar catalogo luego de ingresar la opcion
        # Primer 'for' para obtener clave principal y valor(diccionario)
        for k, v in catalogo.items():
            print("="*60)
            print("TITULO:",k)
            # Segundo 'for' para iterar los elementos dentro del diccionario
            for k1, v1 in v.items():
                #  Si la clave es 'genero' se transforma el valor de cadena a un string separado por comas
                if k1=="genero":
                    print(f"{k1.upper()}: {", ".join(v1)}")
                # De clo contrario solo muestra la clave en mayuscula seguido de su valor
                elif k1=="comentario" and len(v1.strip())==0:
                    print(f"{k1.upper()}: Sin comentarios")
                else:
                    print(f"{k1.upper()}: {v1}")
            print("="*60) # Espacio entre elementos del catalogo


def agregar(catalogo):
    print("Movie serie")

def eliminar(catalogo,titulo):
    for k, v in catalogo.items():
        # Se valida en el bucle que el titutlo ingresado
        # coincida con el titulo del catalogo
        if k==titulo:
            # De coincidir se elimina y se retorna luego de ejecutar la accion
            del catalogo[k]
            print(f"{v["tipo"]} {k} eliminado")
            return
    # Si no se encuentra el titulo deveulve mensaje
    print("No existe pelicula o serie")

def buscar(catalogo):
    print("Movie serie")

def actualiza_valoracion(catalogo, titulo, nuevo_valor):
    for k, v in catalogo.items():
        # Se valida en el bucle que el titutlo ingresado
        # coincida con el titulo del catalogo
        if k==titulo:
            # De coincidir se actualiza y se retorna luego de ejecutar la accion
            v["valoracion"]=nuevo_valor
            print(f"{v["tipo"]} {k} actualizado")
            return
    # Si no se encuentra el titulo deveulve mensaje
    print("No existe pelicula o serie")

def filtrar_genero(catalogo):
    print("Movie serie")

def mostrar_mejores(catalogo):
    print("Movie serie")

