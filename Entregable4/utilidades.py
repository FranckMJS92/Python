# Solicita la entrada de una cadena de texto
# La funcion tiene la opcion de validar o no si la cadena se entrega vacia
# Esta implementacion pensada para el ingreso de los comentarios
def pedir_texto_validacion(mensaje, keep=True):
    while True:
        valor = input(mensaje)
        # Quita espacios antes de validar longitud
        # Si solo ingresa un espacio lo vuelve una cadena vacia
        valor = valor.strip()
        if not keep:
            return valor
        else:
            if len(valor) > 0:
                valor = valor.lower().title()
                return valor
            else:
                print("No puede ser vacio")

# Peticion de texto especial
# Peticion de entrada de texto indicando 2 opciones posibles
def pedir_texto_opcion(mensaje, opcion1="", opcion2=""):
    while True:
        tipo = input(mensaje)
        # Quita espacios antes de validar longitud
        # Si solo ingresa un espacio lo vuelve una cadena vacia
        tipo = tipo.strip()
        if len(tipo) > 0:
            tipo = tipo.lower().title()
            if tipo == opcion1 or tipo == opcion2:
                return tipo
            else:
                print(f"Las opciones son {opcion1} o {opcion2}")
        else:
            print("No puede ser vacio")

# Solicita la entrada de un numero entero en el rango indicado
# Y valida que sea del tipo que se especificado
def pedir_numero_rango(mensaje, min=0, max=1, tipo="int"):
    while True:
        try:
            if tipo == "int":
                valor = int(input(mensaje))
            else:
                valor = float(input(mensaje))
            if max >= valor >= min:
                return valor
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except ValueError:
            print("El valor no es numero valido")

# Peticion de texto especial
# El titulo debe validarse que no se encuentra ya en el catalogo
# De cumplirse la condicion se retorna el valor ingresado por el usuario
def pedir_titulo(mensaje, catalogo):
    # Extraigo los titulos a una lista
    lista_titulos = []
    for k,v in catalogo.items():
        lista_titulos.append(k)

    while True:
        valor = input(mensaje)
        # Quita espacios antes de validar longitud
        # Si solo ingresa un espacio lo vuelve una cadena vacia
        valor = valor.strip()
        if len(valor) > 0:
            valor = valor.lower().title()
            # Validacion que el titulo ingresado no coincida con titulo del catalogo
            if valor in lista_titulos:
                print("El titulo ya se encuentra en el catalogo")
            else:
                return valor
        else:
            print("No puede ser vacio")

# Peticion de texto especial
# El genero es una lista por lo tanto debe permitir ingresar mas de un valor
# Se guarda en una lista para ser agregado al catalogo
def pedir_genero(mensaje):
    genero = []
    while True:
        valor = pedir_texto_validacion(mensaje)
        genero.append(valor)
        seguir = pedir_texto_opcion("Desea agregar otro genero? (S/N) : ","S","N")
        if seguir == "N":
            return genero

# Funcion general para mostrar por consola catalogo
def mostrar_diccionario(k,v):
    print("\n" + "=" * 60)
    print("TITULO:", k)
    # Segundo 'for' para iterar los elementos dentro del diccionario
    for k1, v1 in v.items():
        #  Si la clave es 'genero' se transforma el valor de cadena a un string separado por comas
        if k1 == "genero":
            print(f"{k1.upper()}: {", ".join(v1)}")
        # De lo contrario solo muestra la clave en mayuscula seguido de su valor
        elif k1 == "comentario" and len(v1.strip()) == 0:
            print(f"{k1.upper()}: Sin comentarios")
        else:
            print(f"{k1.upper()}: {v1}")
    print("=" * 60)

# Funcion para mostrar el menu
def mostrar_menu():
        print("\n============ MENU OPCIONES ============")
        print("1.- Mostrar todos")
        print("2.- Agregar serie/película")
        print("3.- Eliminar serie/película")
        print("4.- Buscar serie/película")
        print("5.- Actualizar valoración")
        print("6.- Filtrar por género")
        print("7.- Mostrar mejores series/peliculas")
        print("8.- Salir")