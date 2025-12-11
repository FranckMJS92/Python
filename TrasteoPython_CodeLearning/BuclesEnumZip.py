# BUCLES

# for
for char in "code":
    print(char)

# while
""" secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-5): "))
    if guess != secret_number:
        print("Wrong! Try again.")

print("You got it!") """


developer_names = ["Jess", "Naomi", "Tom"]

for developer in developer_names:
    if developer == "Naomi":
        continue
    print(developer)


words = ["sky", "apple", "rhythm", "fly", "orange"]

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


# range es usado para generar una secuencia de enteros
# sintaxis: range(start, stop, step)
for num in range(3):
    print(num)  # 0 1 2

for num in range(1, 5):
    print(num)  # 1 2 3 4

for num in range(2, 11, 2):
    print(num)  # 2 4 6 8 10

# creando lista con range
numbers = list(range(2, 11, 2))
print(numbers)  # [2, 4, 6, 8, 10]


# ENUMERATED
# es una lista de tuplas

languages = ["Spanish", "English", "Russian", "Chinese"]

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

languages = ["Spanish", "English", "Russian", "Chinese"]

for index, language in enumerate(languages):
    print(f"Index {index} and language {language}")

"""
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese"""

for index, language in enumerate(languages, 1):
    print(f"Index {index} and language {language}")
"""
Index 1 and language Spanish
Index 2 and language English
Index 3 and language Russian
Index 4 and language Chinese"""

# ZIP()
developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]


for name, id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {id}")
"""
Name: Naomi
ID: 1
Name: Dario
ID: 2
Name: Jessica
ID: 3
Name: Tom
ID: 4"""

# filter()
words = ["tree", "sky", "mountain", "river", "cloud", "sun"]


def is_long_word(word):
    return len(word) > 4


long_words = list(filter(is_long_word, words))
print(long_words)  # ['mountain', 'river', 'cloud']

# map()
celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# sum()
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total)  # Result: 50

numbers = [5, 10, 15, 20]
total = sum(numbers, 10)  # valor inicial de sum -> 10
# total = sum(numbers, start=10) # keyword argument
print(total)  # 60

#COMPRESION DE LISTAS ...