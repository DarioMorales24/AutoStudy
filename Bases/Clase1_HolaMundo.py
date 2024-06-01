import os
os.system("cls")

# ==========
# HOLA MUNDO
# ==========

print("Hola mundo")  #Print imprime lo que este dentro en la consola
print ("Hola " + "Mundo") # Con el + puedes añadir o concatenar tipos de textos o numeros

# <- este simbolo es para poner comentarios sirve para añadir texto que el programa no lee

"""
Este es un comentario en varias lineas
hola 
mundo
"""

# Ej: "Hola' esto daría error

#tipos de datos


# String o cadena de texto van con "" o '' pero no pueden ir combinados EJ:
    # "Hola", "Hola como estas?"
# Numeros que pueden ser Integer(Enteros), Float(Reales), Complex(Complejos 3 + 1j)
    # 1 <- int  //  2.64 <- float  //  4 + 6j <- complex
# Booleans es un tipo de dato que dice si algo es True(Verdadero) o False(Falso)
    # True or False
# List es un tipo de dato que agrupa varios datos ej 
    # [0, 1, 2, 3, 4], ["banana", "Melon", "Sandia"], ["banana", 1, "Melon", 2]
# Diccionary es un tipo de dato que agrupa valores o definiciones ej:
"""
mi_diccionario = {
"Palabra1": "valor1"
"Palabra2": "valor2"
"Palabra3": "valor3"
}

print(mi_diccionario["Palabra1"]) esto imprime valor1
"""
#Tuple es una lista en la cual no puedes cambiar los datos dentro de ella los deja definidos y fijos Ej:

"""
mi_tupla = (1, 2, 3, a, b, c)

print(mi_tupla[0]) esto imprime "1"
print(mi_tupla[4]) esto imprime "b"
"""

# Set es una forma de agrupar datos desordenados y mutables, es basicamente una lista desordenada que usualmente sirve para verificar si un dato pertenece o esta en el set Ej:

"""
mi_set = (1, 2, 3, 4, 5)

mi_set.add(6) con el comando .add agregas un dato al sett

print(3 in mi_set) esto imprimirá True ya que 3 está en el set
print(8 in mi_set) esto imprimirá False ya que 8 no está en el set
"""

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Para consultar el tipo de dato puedes usar
print(type("Hola")) # esto imprimira class "str"
print(type(8)) # esto imprimira class "int"
print(type(2.45)) # esto imprimira class "float"
print(type(1 + 4j)) # esto imprimira class "complex"
print(type([1, 2, 3])) # esto imprimira class "list"
print(type({"name": "Alvaro"})) # esto imprimira class "dict"
print(type({9.5, 2.4, 7.0})) # esto imprimira class "set"
print(type((6.7, 5.2, 4, 7.9))) # esto imprimira class "tuple"