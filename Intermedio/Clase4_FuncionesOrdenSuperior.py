import os
os.system("cls")

# FUNCIONES DE ORDEN SUPERIOR

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values(first_value,second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values(2, 4, sum_one))
print(sum_two_values(2, 4, sum_five))

# CLOSURES

# Es una funcion que retorna una funcion 

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()

print(add_closure(3))

def exterior(x):
    def interior(y):
        return x + y
    return interior

# Creamos una función a partir de exterior
agregar_5 = exterior(5)

# Llamamos a la función interna
print(agregar_5(3))  # Output: 8

# Lo importante a destacar aquí es que interior() 
# aún recuerda el valor de x incluso después de que exterior()
# ha terminado de ejecutarse. Este comportamiento es lo que define
# una closure en Python: la capacidad de una función interna de 
# recordar y acceder al ámbito de la función externa en la que fue definida

print(exterior(5)(3)) # esta es otra manera de llamar closures 

# Funciondes de orden superior internas

numbers = [2, 5, 10, 21, 3, 30]

# Map  <- esto siempre necesita un conjunto iterable

# map es una funcion que ejecuta una funcion con una lista de elementos, map(funcion, conjunto)
def mult(number):
    return number * 2

print(map(mult, numbers)) # <- esto arroja un objeto

numers_mult = list(map(mult, numbers))
print(numers_mult) # <- para observarlo lo agregamos a una lista

numers_mult = list(map(lambda number: number * 2, numbers)) # <- aqui usamos una lambda dentro de un map
print(numers_mult)

# Filter <- es una funcion que retorna true o false para filtrar items dentro de un conjunto de datos, filter(funcion, conjunto)

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers))) 

print(list(filter(lambda number: number > 10, numbers)))

# Reduce  <- esto opera con los valores que va recorriendo en el iterable hasta reducirlo a 1 unico valor
from functools import reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))

print(reduce(lambda first_value, second_value: first_value + second_value, numbers))
