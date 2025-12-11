my_int_1 = 56
my_int_2 = 12

# Division
div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 4.666666666666667
print(type(div_ints))

# modulo de int y float -> %
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulus:', mod_ints) # Integer Modulus: 8
print('Float Modulus:', mod_floats) # Float Modulus: 1.1999999999999993

# division exacta -> //
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0

# Potenciacion -> **
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089

# round(): Redondea un número al número especificado de decimales.
# Por defecto, esta función redondea al entero más cercano y devuelve un número entero sin decimales
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# abs(): devuelve el valor absoluto de un número,
num = -15

absolute_value = abs(num)
print(absolute_value) # 15

# bin(): convierte un entero en su representación binaria como una cadena.
# oct(): convierte un entero en su representación octal como una cadena.
# hex(): convierte un entero en su representación hexadecimal como una cadena.
my_int = 56

binary_representation = bin(my_int)
print(binary_representation)  # 0b111000

octal_representation = oct(my_int)
print(octal_representation) # 0o70

hex_representation = hex(my_int)
print(hex_representation) # 0x38

# pow(): eleva un número a la potencia de otro o realiza la exponenciación modular.
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3