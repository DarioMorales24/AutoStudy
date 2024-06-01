import os
os.system("cls")

# STRINGS

my_string = "My string"
my_other_string = 'My other string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapando"
print(my_scape_string)

# Formateo

name, surname, age = "Dario", "Morales", 24
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age)) # <- esta te ayuda a ver errores de formato

print(f"Mi nombre es {name} {surname} y mi edad es {age}") # <- esta es la mejor manera

# Desempaquetado de caracteres

language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_languaje = language[:: -1]
print(reversed_languaje)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())

