import os
os.system("cls")

# OPERADORES

# OPERADORES ARITMETICOS

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)

6 + 10 # <- esto es una suma que no se guarda en ningun lado asi que es como si no existiera

print(10 % 3) # <- modulo o te revisa si en una divison existe un resto
print(10 // 3) # <- esta es una division que siempre nos dara un numero entero aproximado
print(2 ** 3) # <- exponente o 2 elevado a 3

print("Hola" + "Python") # <- el simbolo + sirve para concatenar igualmente, pero no se puede entre tipos distintos
# print("Hola" + 5) # <- esto dará error
print("Hola" + str(5)) # <- asi si se puede

# OPERADORES COMPARATIVOS

print(3 < 4)
print(4 <= 4)
print(3 > 4)
print(4 >= 4)
print(3 == 4)
print(3 != 4)

#Sus resultados seran booleanos
print("---------------------------------")

print("Hola" <  "Python")
print("Hola" <= "Python")
print("Hola" >  "Python")
print("Hola" >= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

#Aqui compara la ordenación alfabetica incluyendo las mayusculas ¡¡NO!! la cantidad de caracteres 
print("---------------------------------")
# OPERADORES LOGICOS

#AND
print ((3 < 4) and ("Hola" <  "Python")) # Verdadero y Verdadero = Verdadero
print ((3 < 4) and ("Hola" >  "Python")) #Verdadero y Falso = Falso
print ((3 > 4) and ("Hola" >  "Python")) #Falso y Falso = Falso
print ((3 > 4) and ("Hola" <  "Python")) #Falso y Verdadero = Falso
print("---------------------------------")

#OR
print ((3 < 4) or ("Hola" <  "Python")) #Verdadero o Verdadero = Verdadero
print ((3 < 4) or ("Hola" >  "Python")) #Verdadero o Falso = Verdadero
print ((3 > 4) or ("Hola" >  "Python")) #Falso o Falso = Falso
print ((3 > 4) or ("Hola" <  "Python")) #Falso o Verdadero = Verdadero
print("---------------------------------")

#NOT
print(not(3 > 4)) #Aqui es la negacion a la verdad es decir 3 > 4 es falso pero al decir not false = True (es decir es lo opuesto)










