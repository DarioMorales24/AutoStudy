import os
os.system("cls")

# BUCLES

# While

my_condition = 0

while my_condition < 10: # <- mientras la condicion sea verdad se va a ejecutar lo de abajo
    print(my_condition)
    my_condition += 2 # <- con el += es lo mismo que var = var + 1
#if my_condition == 10:                             <- al agregar un if entre while y else if se roba al else pero si no se encuentra, el else pasa a ser del while
#    print("Mi condicion es igual a 10")
else: 
    print("Mi condicion es mayor o igual que 10")


print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
        break                           # <- break sirve para detener el bucle de manera forzada
    print(my_condition)

print("La ejecucion continua")


# For

my_list = [23, 1999, 45, 32, 24, 9, 16]

for element in my_list:  # <- este bucle va recorriendo elemento por elemento de la lista, estructura , etc que le estemos pidiendo que evalúe
    print(element)

my_tuple = (24, 1.73, "Dario", "Morales", "Soulmates")

for element in my_tuple: 
    print(element)

my_set = {"Dario", "Morales", 24}

for element in my_set: 
    print(element)

my_dict = {"Nombre": "Dario", "Apellido": "Morales", "Edad": 24, "Nick": "Soulmates"}

for element in my_dict: 
    print(element)
    if element == "Edad":
        break   # <- el break corta todo lo que esta abajo si se cumple la condicion
        print("Se ejecuta")
    elif element == "Nick":
        print("element vale Nick")
    else:
        print("Chao")
else:
    print("El bucle for para mi diccionario ha finalizado")

for element in my_dict: 
    print(element)
    if element == "Edad":
        continue               # <- ¡¡¡¡¡OJO NO SE RECOMIENDA!!!!  el continue corta lo que sigue y empieza del siguiente element desde el comienzo
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")