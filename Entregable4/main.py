from Entregable4.series import *

# Declaracion de diccionario para el CRUD, con data inicial
catalogo = {
    "The Shawshank Redemption": {
        "tipo": "Película",
        "genero": ["Drama"],
        "year": 1994,
        "valoracion": 9.3,
        "comentario": "Obra maestra del cine"
    },
    "Inception": {
        "tipo": "Película",
        "genero": ["Ciencia ficción", "Acción", "Suspenso"],
        "year": 2010,
        "valoracion": 8.8,
        "comentario": ""
    },
    "Stranger Things": {
        "tipo": "Serie",
        "genero": ["Ciencia ficción", "Terror", "Suspenso"],
        "year": 2016,
        "valoracion": 8.7,
        "comentario": "Serie muy popular de Netflix"
    },
    "The Office": {
        "tipo": "Serie",
        "genero": ["Comedia"],
        "year": 2005,
        "valoracion": 8.9,
        "comentario": ""
    },
    "Parasite": {
        "tipo": "Película",
        "genero": ["Drama", "Suspenso", "Comedia"],
        "year": 2019,
        "valoracion": 8.6,
        "comentario": "Primera película no inglesa en ganar el Oscar"
    }
}

while True:
    mostrar_menu()

    opcion = pedir_entero_rango("Indica tu opción: ",1,8)

    match opcion:
        case 1:
            mostrar_todos(catalogo)
        case 2:
            agregar(catalogo)
        case 3:
            titulo = pedir_texto("Ingrese titulo a eliminar: ")
            eliminar(catalogo,titulo)
        case 4:
            buscar(catalogo)
        case 5:
            titulo = pedir_texto("Ingrese titulo para modificar su valoracion: ")
            nuevo_valor = pedir_float("Ingrese valor a modificar: ")
            actualiza_valoracion(catalogo, titulo, nuevo_valor)
        case 6:
            filtrar_genero(catalogo)
        case 7:
            mostrar_mejores(catalogo)
        case 8:
            print("Hasta la proxima!!!!")
            # Salimos del bucle
            break
        case _:
            print("Opcion invalida")
