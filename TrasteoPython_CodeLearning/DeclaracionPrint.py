name = 'John Doe'
age = 25

# Variables en minuscula separados por _ (snake_case)
my_variable_name = 'freeCodeCamp'
user_age = 30

x = 56 # What do you mean by x?
#5variable_name = 5 #declaracion no valida

# This is a single-line comment

# This is a
# multi-line
# comment

print('Hello world!') # Hello world!

# Output: My favorite colors are blue green red
print('My favorite colors are', 'blue', 'green', 'red')


my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>

# isinstance() Toma un objeto y el tipo contra el que quieres comprobarlo,
# y luego devuelve un booleano. Aquí tienes algunos ejemplos:
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False

# Pistas de tipo
# Python solo usa estas pistas para análisis estático, 
# documentación y soporte de editores, no para hacer cumplir tipos durante la ejecución. 
user_name: str = 'John Doe'
user_age: int = 24