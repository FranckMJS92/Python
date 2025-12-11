# TUPLA

developer = ("Alice", 34, "Rust Developer")

programming_languages = ("Python", "Java", "C++", "Rust")
# programming_languages[0] = 'JavaScript' -> son inmutables

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""

# Usando constructor
developer = "Jessica"
t1 = tuple(developer)  # ('J', 'e', 's', 's', 'i', 'c', 'a')

desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3])

# por entender...
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']