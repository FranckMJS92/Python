from Entregable4.utilidades import *

def mostrar_todos(catalogo):
    # Si catalogo esta vacio devuelve mensaje
    if len(catalogo) == 0:
        print("No existen peliculas o series")
    else:
        # Primer 'for' para obtener clave principal y valor(diccionario)
        for k, v in catalogo.items():
            mostrar_diccionario(k, v)

def agregar(catalogo, titulo,tipo,genero,year,valoracion,comentario):
    catalogo[titulo] = {
        "tipo" : tipo,
        "genero" : genero,
        "year" : year,
        "valoracion" : valoracion,
        "comentario" : comentario
         }
    print(f"\n{tipo} {titulo} ahora se encuentra en el catalogo")

def eliminar_titulo(catalogo,titulo):
    for k, v in catalogo.items():
        # Se valida en el bucle que el titutlo ingresado
        # coincida con el titulo del catalogo
        if k==titulo:
            # De coincidir se elimina y se retorna luego de ejecutar la accion
            del catalogo[k]
            print(f"\n Correcto, {v["tipo"]} {k} ya no se encuentra en el catalogo")
            return
    # Si no se encuentra el titulo deveulve mensaje
    print(f"\nNo existe pelicula o serie {titulo}")

def buscar_titulo(catalogo, titulo):
    for k, v in catalogo.items():
        # Se valida en el bucle que el titutlo ingresado
        # coincida con el titulo del catalogo
        if k == titulo:
            # De coincidir se muestra por consola
            mostrar_diccionario(k,v)
            return
    # Si no se encuentra el titulo deveulve mensaje
    print(f"\nNo existe pelicula o serie {titulo}")

def actualiza_valoracion(catalogo, titulo, nuevo_valor):
    for k, v in catalogo.items():
        # Se valida en el bucle que el titutlo ingresado
        # coincida con el titulo del catalogo
        if k==titulo:
            # De coincidir se actualiza y se retorna luego de ejecutar la accion
            v["valoracion"]=nuevo_valor
            print(f"\n{v["tipo"]} {k} actualizada")
            return
    # Si no se encuentra el titulo deveulve mensaje
    print("\n No existe pelicula o serie")

def filtrar_genero(catalogo,genero):
    # Variable para saber cantidad de coincidencias
    count=0
    # bucle para iterar entre los elementos del catalogo
    for k, v in catalogo.items():
        for k1,v1 in v.items():
            # Condicional para evaluar si la clave
            # de diccionario anidado es "genero"
            if k1 == "genero":
                # Si el genero indicado por usuario
                # se encuentra en la lista de valores de clave "genero"
                if genero in v1:
                    count+=1
                    mostrar_diccionario(k,v)

    if count==0:
        # Si no encuentra coincidencia indica por mensaje
        print(f"\nNo se encontro pelicula o serie con genero: {genero}")

def mostrar_mejores(catalogo):
    # Variable para saber cuantas peliculas/series cumplen condicion
    count_best=0
    # Bucle para recorrer catalogo
    for k, v in catalogo.items():
        for k1, v1 in v.items():
            # Cuando la clave del subdiccionario sea "valoracion"
            # Se evalua el value
            if k1 == "valoracion":
                if v1>=9:
                    # De cumplirse se suma 1 a variable
                    count_best+=1
                    # Y se muestra en consola
                    mostrar_diccionario(k,v)
    # De no encontrarse pelicula o serie, se devuelve mensaje indicandolo
    if count_best==0:
        print("\nNinguna pelicula o serie cumple la condicion")