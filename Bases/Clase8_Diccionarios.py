import os
os.system("cls")

# DICCIONARIOS

my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre": "Dario", "Apellido": "Morales", "Edad": 24, 1:"Python"}
my_dict = {
    "Nombre": "Dario",
    "Apellido": "Morales", 
    "Edad": 24, 
    "Lenguajes":{"Python", "Html", "CSS"},
    1: 1.73
}

print(my_dict)
print(len(my_dict)) # <- esto imprime la cantidad de claves dentro del diccionario

print(my_dict["Nombre"]) # <- con esto imprime el valor de la clave "Nombre"

my_dict["Nombre"] = "Soulmates" #<- con esta manera puedes actualizar el valor de una clave
my_dict["Nombre"] = "Dario"

my_dict["Calle"] = "Socoroma" # <- asi agregamos claves y sus valores dentro del diccionario
print(my_dict)

del my_dict["Calle"]# <- asi eliminas una clave del deccionario
print(my_dict)

print("Dario" in my_dict) # <- esto nos dice false ya que de esta forma buscamos por clave
print("Dario" in my_dict["Nombre"]) # <- asi puedes buscar algo dentro de las claves

print(my_dict.items()) # <- con esta opcion nos da las claves y sus valores de los diccionaarios
print(my_dict.keys()) # <- Asi solo nos da las claves del diccionario
print(my_dict.values()) # <- Asi solo nos da los valores de las claves del diccionario


# my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
# print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list) # <- con esta opcion copias las claves de un diccionario
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, my_dict)
print(my_new_dict)
print(list(my_new_dict))