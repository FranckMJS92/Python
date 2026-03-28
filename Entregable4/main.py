from Entregable4.series import *
from Entregable4.utilidades import *

# Declaracion de diccionario para el CRUD, con data inicial
catalogo = {
    "The Shawshank Redemption": {
        "tipo": "Pelicula",
        "genero": ["Drama"],
        "year": 1994,
        "valoracion": 9.3,
        "comentario": "Obra maestra del cine"
    },
    "Inception": {
        "tipo": "Pelicula",
        "genero": ["Ciencia ficcion", "Accion", "Suspenso"],
        "year": 2010,
        "valoracion": 8.8,
        "comentario": ""
    },
    "Stranger Things": {
        "tipo": "Serie",
        "genero": ["Ciencia ficcion", "Terror", "Suspenso"],
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
        "tipo": "Pelicula",
        "genero": ["Drama", "Suspenso", "Comedia"],
        "year": 2019,
        "valoracion": 8.6,
        "comentario": "Primera película no inglesa en ganar el Oscar"
    }
}

while True:
    mostrar_menu()

    opcion = pedir_numero_rango("Indica tu opción: ",1,8)

    match opcion:
        case 1:
            mostrar_todos(catalogo)
        case 2:
            print("\nDATOS PARA CATALOGO")
            print("="*60)
            titulo_valida = pedir_titulo("Ingrese titulo: ",catalogo)
            tipo = pedir_texto_opcion("Ingrese Tipo: (Serie / Pelicula) ","Serie","Pelicula")
            genero = pedir_genero("Ingrese Genero: ")
            year = pedir_numero_rango("Ingrese año: ",1895,2026) # Año de la primera pelicula registrada 1895 : La Sortie de l'Usine Lumière à Lyon
            valoracion = pedir_numero_rango("Ingrese valoracion: ",0,10,"float")
            comentario = pedir_texto_validacion("Ingrese comentario: ",False) # Comentario puede estar vacio
            agregar(catalogo, titulo_valida,tipo,genero,year,valoracion,comentario)
        case 3:
            titulo_delete = pedir_texto_validacion("Ingrese titulo a eliminar: ")
            eliminar_titulo(catalogo,titulo_delete)
        case 4:
            titulo_search = pedir_texto_validacion("Ingrese titulo a buscar: ")
            buscar_titulo(catalogo, titulo_search)
        case 5:
            titulo_valora = pedir_texto_validacion("Ingrese titulo para modificar su valoracion: ")
            nuevo_valor = pedir_numero_rango("Ingrese valoracion para modificar: ",0,10,"float")
            actualiza_valoracion(catalogo, titulo_valora, nuevo_valor)
        case 6:
            genero_filter = pedir_texto_validacion("Ingrese genero a filtrar: ")
            filtrar_genero(catalogo, genero_filter)
        case 7:
            n = pedir_numero_rango("Ingrese cuantos registros desea: ", 1, len(catalogo))
            mejores_n(catalogo, n)
        case 8:
            print("\nHasta la proxima!!!!")
            # Salimos del bucle
            break
        case _:
            print("Opcion invalida")
