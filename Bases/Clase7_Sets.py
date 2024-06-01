import os
os.system("cls")

# SETS

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # <- segun esto nos dice que es un diccionario

my_other_set = {"Dario", "Morales", 24}
print(type(my_other_set)) # <- ahora aparecce como que es un set

print(len(my_other_set))

my_other_set.add("Soulmates")
print(my_other_set) # <- un set no es una estructura ordenada

my_other_set.add("Soulmates")
print(my_other_set) # <- un set no admite elementos repetidos

print("Dario" in my_other_set)
print("Darioo" in my_other_set) # <- podemos buscar datos dentro de los sets

my_other_set.remove("Soulmates") # <- puedes elimiar datos del set
print(my_other_set)

my_other_set.clear() # <- esto elimina todos los datos de un set
print(my_other_set)
print(len(my_other_set))

# del my_other_set  <- elimina al set desde la variable donde fue guardada 
# print(my_other_set)

my_set = {"Dario", "Morales", 24}
my_list = list(my_set)

print(my_list)
print(my_list[0])

my_other_set = {"Html", "CSS", "Python"}

my_new_set = my_set.union(my_other_set).union({"Lol", "Valorant"})
print(my_new_set)

print(my_new_set.difference(my_set)) # <- esto busca las diferencias entre los dos sets

# print(my_other_set[1]) <- esto da error

