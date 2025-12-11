# LISTAS
cities = ["Los Angeles", "London", "Tokyo"]
cities[0]  # 'Los Angeles'

cities[-1]  # 'Tokyo'

# Usando constructor list()
developer = "Jessica"
list(developer)  # ['J', 'e', 's', 's', 'i', 'c', 'a']

# Numeros elementos
numbers = [1, 2, 3, 4, 5]
len(numbers)  # 5

# Actualizando list por indice
programming_languages = ["Python", "Java", "C++", "Rust"]
programming_languages[0] = "JavaScript"
print(programming_languages)  # ['JavaScript', 'Java', 'C++', 'Rust']

# Eliminar elemento
developer = ["Jane Doe", 23, "Python Developer"]
del developer[1]
print(developer)  # ['Jane Doe', 'Python Developer']

# Comprobando que existe un elemento con in
programming_languages = ["Python", "Java", "C++", "Rust"]
"Rust" in programming_languages  # True
"JavaScript" in programming_languages  # False

# Lista anidada
developer = ["Alice", 25, ["Python", "Rust", "C++"]]
developer[2]  # ['Python', 'Rust', 'C++']
developer[2][1]  # 'Rust'

# Unpacking valores de una lista a variables
developer = ["Alice", 34, "Rust Developer"]
name, age, job = developer

print(name)  # 'Alice'
print(age)  # 34
print(job)  # 'Rust Developer'

# Unpacking usando *[variable]
developer = ["Alice", 34, "Rust Developer"]
name, *rest = developer

print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']

# Operador de corte :
desserts = ["Cake", "Cookies", "Ice Cream", "Pie", "Brownies"]
desserts[1:4]  # ['Cookies', 'Ice Cream', 'Pie']

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2]  # [2, 4, 6]

# append añade elemento al final, tambien se puede añadir otra lista
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

# numbers.append(even_numbers)
print(numbers)  # [1, 2, 3, 4, 5, [6, 8, 10]]

# extends
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers)  # [1, 2, 3, 4, 5, 6, 8, 10]

# insert, si todos los elementos son de un tipo insert solo puede insertar ee tipo
numbers = [1, 2, 3, 4, 6.3, 5]
numbers.insert(2, 2.4)

print(numbers)  # [1, 2, 2.4, 3, 4, 5]

# Este método solo elimina la primera aparición de un elemento. No todos
numbers = [1, 2, 3, 4, 5, 5, 5]
numbers.remove(5)

print(numbers)  # [1, 2, 3, 4, 5, 5]

# pop elimina por indice, si no se indica elimina el ultimo elemento
numbers = [1, 2, 3, 4, 5]
numbers.pop(1)  # The number 2 is returned

# Vaciar la lista
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers)  # []

# Ordena la lista
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers)  # [1, 2, 19, 35, 41, 67]

# sorted() devuelve una nueva lista ordenada
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers)  # [19, 2, 35, 1, 67, 41]
print(sorted_numbers)  # [1, 2, 19, 35, 41, 67]

# Invertir lista
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers)  # [1, 2, 3, 4, 5, 6]

# index devuelve posicion de elemento
programming_languages = ["Rust", "Java", "Python", "C++"]
programming_languages.index("Java")  # 1
