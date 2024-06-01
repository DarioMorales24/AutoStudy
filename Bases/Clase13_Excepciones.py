import os
os.system("cls")

# EXCEPCIONES

"""
Try:
    {Ejecuta este codigo}
except:
    {Ejecuta este codigo si existe una excepcion}
else: 
    {Sin excepciones? Ejecuta este codigo}
finally:
    {Siempre ejecuta este codigo}

"""
number_one = 5
number_two = 1
number_two = "1"

# Try Except
try:
    print(number_one + number_two)  # <- Esto da error
    print("No se ha producido error")
except:
    print("Se ha producido un error")


# Try Except Else
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:                                             # <- esto se ejecuta si no se produce una excepcion
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")

# Try Except Else Finaly

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")
finally:                                            # <- Se ejecuta siempre
    print("La ejecucion continua")


# Excepciones por tipos

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except TypeError:                       # <- Aqui except solo se ejecuta si hay un TypeError
    print("Se ha producido un TypeError")
except ValueError:                       # <- Podemos añadir distintos except para tener distintos errores
    print("Se ha producido un ValueError")


# Captura de la informacion de la excepcion

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:             # <- con la propiedad as "Nombre de la variable" te guarda la razon de porque surguio el error
    print(error)
except Exception as exception:          # <- con la propiedad Exception sirve para ejecutar la excepcion si existe alguna excepcion
    print(exception)                    # <- en este caso como el error es TypeError ejecuta el except de Exception y no el de ValueError
