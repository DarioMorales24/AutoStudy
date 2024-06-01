import os
os.system("cls")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TIPOS DE ERRORES
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - SyntaxError -

# print "Holas" <- esto arroja un SyntaxError o un error de sintaxis
print("Hola")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - NameError -

# print(name)  <- esto arroja un NameError o error de nombre, esto es porque la variable name no esta definido o esta mal escrito

name = "Soy Gokú"
print(name)   # <- ahora funciona ya que arriba de esta linea si existe una variable llamada nombre

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - IndexError -

my_list = ["Hola", "Soy", "Gokú"]
# print(my_list[3])  <- esto arroja un IndexError o error de indice ya que no exite en la lista un elemento con ese indice ya que todas las listas comienzan del 0
print(my_list[0])
print(my_list[1])
print(my_list[2])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - ModuleNotFoundError -

# import maths <- esto arroja un ModuleNotFoundError ya que no exite un modulo llamado maths
import math

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - AttributeError -

# print(math.pis) <- esto da un AttributeError ya que dentro del modulo math no existe un atributo llamado PermissionError
print(math.pi)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - KeyError -

my_dict = {"nombre":"Gokú", "Apellido":"son"}
# print(my_dict["Saludo"])  <- aqui hay un KeyError ya que no existe una clave "Saludo" dentro del diccionario my_dict
print(my_dict["Apellido"]) 
print(my_dict["nombre"])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - TypeError - 

# print(my_list["Nombre"]) <- esto da un error ya que no existe ni puede haber un indice como string 
print(f"{my_list[0]} {my_list[1]} {my_list[2]}")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - ImportError -

# from math import pis <- esto da un ImportError ya que no se encontro un atributo pis dentro de math
from math import pi
print(pi)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - ValueError - 

# my_int = int("10 años") <- esto no se puede ya que "10 años" no se puede transformar a un entero
my_int = int("10")
print(my_int)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - ZeroDivisionError - 

print(2/4)
# print(2/0) <- esto da ZeroDivisionError ya que no se puede dividir por cero