import os
os.system("cls")

# FUNCIONES  <- estas sirven para poder llamar a una seccion del comando para ahorrar codigo y errores

def my_function ():    # <- asi se define una funcion  def "Nombre de la funcion" ():
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_number, second_number):  # <- Aqui le asignamos dos parametros a la funcion estos son obligatorios para llamar a la funcion
    print(first_number + second_number)

# sum_two_values()  <- aqui llamamos a la funcion sin parametros y nos arroja error
sum_two_values(5,7)  # <- aqui le asignamos los parametros first_number = 5 y second_number = 7
sum_two_values(2131232331,231343445667678)
sum_two_values(1.3,5.6)
sum_two_values("5","7")


def sum_two_values_with_return (first_number, second_number): 
    return first_number + second_number  # <- esto devuelve algo al codigo en este caso devuelve la suma de ambos numeros

my_result = sum_two_values_with_return(10,5)
# my_result = sum_two_values(2,3)  <- esto no retorna nada 

print(my_result)

def print_name (name, surname):
    print(f"{name} {surname} ")

print_name(surname = "Morales", name = "Dario")

def print_name_with_default (name, surname, alias = "Sin alias"):  # <- al asignarle un valor a alias este se ejecutará si al llamar la funcion no le damos el parametro de alias
    print(f"{name} {surname} {alias}")

print_name_with_default("Dario", "Morales", "Soulmates")
print_name_with_default("Dario", "Morales")  # <- es como si tuviera un repuesto en caso de no tener el parametro deseado

def print_texts (*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "Soulmates")