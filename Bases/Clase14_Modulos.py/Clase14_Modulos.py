import os
os.system("cls")

# ===========
# = MODULOS =
# ===========


#my_function()  # <- esto da error ya que no tenemos definida esta funcion en este codigo


import Clase14_Module # <- con import llamamos a otro codigo de otro archivo, librerias, etc

Clase14_Module.sumValue(1, 2, 3)  # <- para acceder a la funcion sum del otro archivo se tiene que ejecutar en ese archivo
Clase14_Module.print_value("Hola Python")


from Clase14_Module import sumValue, print_value  # <- de esta manera llamamos a una/s funcion/es especifica/s dentro del modulo

sumValue(1, 2, 3)
print_value("Hola Python")

import math  # <- estas son librerias que vienen incorporadas dentro de python

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE # <- con as puedes renombrar una propiedad, constantes, funciones, etc 

print(PI_VALUE)

