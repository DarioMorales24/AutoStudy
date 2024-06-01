import os
os.system("cls")

sum_two_values = lambda first_value, second_value: first_value + second_value # las lambdas son funciones sin nombre
print(sum_two_values(2, 5))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2,3))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(5)(2,4))

