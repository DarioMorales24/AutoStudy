import os
os.system("cls")

# CONDICIONALES

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition > 10 and my_condition <= 20:
    print("Es mayor que 10 y menor o igual que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor que 20 o distinto de 25")

print("La ejecucion continua")

my_string = "Hola"

if my_string:
    print("Mi cadena de texto no es vacia")