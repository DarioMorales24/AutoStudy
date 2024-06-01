import os
os.system("cls")

# VARIABLES

# Las variables siempre son con minusculas y con nombres en texto

myvariable = "My string variable" # <- este es un ejemplo de variable llamada myvariable con valor My string variable
print(myvariable)

my_int_variable = 5  # <- ej de variable entera
print(my_int_variable)

my_bool_variable = True #  <- ej de variable booleana
print(my_bool_variable)

name, surname, nick, age = "Dario", "Morales", "Soulmates", 24  # <- se pueden escribir mas de una variable en una linea ¡¡¡¡¡¡¡ESTO NO ES RECOMENDABLE!!!!!!!
print(f"Me llamo {name} {surname} y mi edad es {age} y mi nick es {nick}")


print(myvariable, my_int_variable, my_bool_variable) # <- con las , puedes concatenar varias variables
print("Este es el valor de :", my_bool_variable)

var = str(4)  # <- con la funcion str() puedes transformar un tipo de dato en tipo str
print(type(var))

print(len(myvariable)) # <- la funcion len cuenta los caracteres de la variable o dato que este en su interior

firstname = input("Ingrese su nombre: ") # <- input es una funcion de entrada es decir que le pide al usuario ingresar un dato al sistema y que este lo guarde en la funcion firstname
age = input("Ingrese su edad: ")

# las variables son reescribibles ya que pueden cambiar su valor a medida que baja el codigo

