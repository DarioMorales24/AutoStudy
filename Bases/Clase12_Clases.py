import os
os.system("cls")

# CLASES

# class Person: <- esto da error si esta vacio

class myEmptyPerson: # <- Asi se define una clase
    pass  # <- esto sirve para poder crear una clase vacia sin que de error

print(myEmptyPerson())
print(myEmptyPerson)

class person :
    def __init__(self, name, surname, alias = "Sin alias") :  # <- con esta funcion sirve para darle parametros a la clase y es obligatiorio para crear una clase
        self.__name = name                  # <- con los dos __ sirve para poner una propiedad privada la cual no se puede modificar
        self.surname = surname              # <- Propiedad publica
        self.full_name = f"{name} {surname} ({alias})"
    
    def get_name(self):
        return(self.__name)

    def walk(self):                                 # <- le podemos agregar una funcion a la clase pero tiene que tener el atributo de self para tomar los datos de la clase
        print(f"{self.full_name} esta caminando")

my_person = person("Dario", "Morales")
print(f"{my_person.get_name} {my_person.surname}")
print(my_person.full_name)

my_person.walk()

my_other_person = person("Dario", "Morales", "Soulmates")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Alvaro Morales (Zorro)" # <- si la clase esta creada para una variable puedes modificar la propiedad como quieras
print(my_other_person.full_name)

print(my_person.get_name())
