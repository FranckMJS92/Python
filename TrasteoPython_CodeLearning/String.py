# Si necesitas una cadena de varias líneas, puedes usar comillas triples dobles o comillas simples:
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

# Usa el tipo de comillas opuestas. Es decir,
# si tu cadena contiene comillas simples, usa comillas dobles para envolver la cadena, y viceversa:
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Concatenacion
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# TypeError: can only concatenate str (not "int") to str
name = 'John Doe'
age = 26
""" 
name_and_age = name + age
print(name_and_age)  """

name_and_age = name + str(age)
print(name_and_age) # John Doe26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

# PRINT F
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

# len : tamaño de la cadena
my_str = 'Hello world'
print(len(my_str))  # 11

print(my_str[0])  # H
print(my_str[6])  # w

# string[start:stop]
print(my_str[1:4]) # ell
print(my_str[:7])  # Hello w
print(my_str[8:])  # rld

# string[start:stop:step]
print(my_str[0:11:2])  # Hlowrd
print(my_str[::-1]) # dlrow olleH

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

# upper(): Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

# lower(): Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.
lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

# strip(): Devuelve una nueva cadena con los caracteres iniciales y finales especificados eliminados.
# Si no se aprueba ningún argumento, elimina los espacios en blanco delanteros y traseros.
my_str_space = '  hello world  '

trimmed_my_str = my_str_space.strip()
print(trimmed_my_str)  # "hello world"

# replace(old, new): Devuelve una nueva cadena con todas las ocurrencias de reemplazadas 
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

# split(separator): Divide una cadena en un separador especificado en una lista de cadenas.
# Si no se especifica ningún separador, se divide en el espacio en blanco.
split_words = my_str.split()
print(split_words)  # ['hello', 'world']

# join(iterable): Une elementos de un iterable en una cadena con un separador.
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

# startswith(prefix): Devuelve un booleano que indica si una cadena comienza con el prefijo especificado.
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

# endswith(suffix): Devuelve un booleano que indica si una cadena termina con el sufijo especificado.
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

# find(substring): Devuelve el índice de la primera aparición de substring, o -1 si no encuentra ninguno.
world_index = my_str.find('world')
print(world_index)  # 6

# count(substring): Devuelve el número de veces que una subcadena aparece en una cadena.
o_count = my_str.count('o')
print(o_count)  # 2

# isupper(): Devuelve true si todas las letras de la cadena son mayúsculas y si no false
is_all_upper = my_str.isupper()
print(is_all_upper)  # False

# islower(): Retorna true si todas las letras de la cadena son minúsculas y si no false
is_all_lower = my_str.islower()
print(is_all_lower)  # True

# title(): Devuelve una nueva cadena con la primera letra de cada palabra en mayúscula.
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World