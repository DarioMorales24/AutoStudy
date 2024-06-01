import os
os.system("cls")

# LISTAS

# Estas son dos maneras de escribir una lista
# my_list = list()  
# my_other_list = []

my_list = [1, 23, 24, 2, 45, 50]

print(my_list)
print(len(my_list)) # <- len es una funcion que evalua el largo de una variable

my_other_list = [24, 1.73, "Dario", "Morales"] # <- una lista puede tener varios tipos de datos

# Una lista tiene mas opciones que un array

print(my_other_list[0]) # <- en las listas el primer elemento es el elemento 0 y los negativos van desde atras a delante
print(my_other_list.count("Morales")) # <- la funcion .count sirve para contar cuantas veces se repite un valor

age, height, name, surname = my_other_list  # <- aqui le asignamos variables a cada elemento dentro de la lista
# age, height, name = my_other_list  # <- esto da error si ponemos menos o mas variables para la cantidad de elementos dentro de la lista 
print(name)
print(my_list + my_other_list) #<- con la suma puedes sumar listas para concatenar sus valores

my_other_list.append("Soulmates") # <- con esta opcion puedes insertar valores a la lista pero solo al final de esta
my_other_list.insert(1, "Rojo") # <- con la funcion .insert puedes insertar valores a la lista con una ubicacion predeterminada
print(my_other_list)

my_other_list.remove("Rojo") # <- con remove elimina un elemento de la lista pero si la lista tiene mas de un elemento del mismo nombre solo borra el primero
print(my_other_list)

my_other_list[1]= "Azul" # <- de esta forma puedes editar algun elemento dentro de la lista
print(my_other_list)

my_new_list = my_other_list.copy() # <- con la funcion copy puedes copiar los valores de una lista en otra variable y no perder los datos si borras o cambias la primera lista
print(my_other_list)
print(my_new_list)

my_list.sort() # <- esta funcion ordena los valores dentro de la lista
print(my_list)

my_list.pop() # <- con la funcion .pop saca de la lista al ultimo valor y se puede ver lo ultimo que se quito de la lista
print(my_list)
print(my_list.pop())

my_list.pop(2) # <- con esta funcion puedes asignar que elemento quitar de la lista

del my_list[2] # <- con del puedes eliminar un elemento de la lista y no guardarlo de ninguna manera
print(my_list)