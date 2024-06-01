import os
os.system("cls")

# TUPLAS

# estas son dos formas de escribir una tupla
my_tuple = tuple()
my_other_tuple = ("lol", "Valorant")

my_tuple = (24, 1.73, "Dario", "Morales")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Dario"))
print(my_tuple.count("Soulmates"))
print(my_tuple.index("Dario")) # <- con idex puedes saber la posicion del valor seleccionado en la lista

# my_tuple[1] = 1.70 # <- las tuplas son unos conjuntos de valores inmutables por lo que no puedes agregar, quitar ni cambiar los elementos dentro de ella
# print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple # <- con + puedes concatenar tuplas y guardarlas en otra variable
print(my_sum_tuple)

my_tuple = list(my_tuple) # <- de esta forma puedes transformar de tupla a lista para poder cambiar los datos de la tupla
print(type(my_tuple))
print(my_tuple)
my_tuple.insert(1, "Rojo")
#----------------------------------------
my_tuple = tuple(my_tuple) # <- asi puedes volver a transformar de lista a tupla
print(type(my_tuple))
print(my_tuple)

del my_tuple # <- con esta forma podemos borrar una variable aunque esta tenga en su interior una tupla
# print(my_tuple) esto da error ya que no encuentra la variable my_tuple

