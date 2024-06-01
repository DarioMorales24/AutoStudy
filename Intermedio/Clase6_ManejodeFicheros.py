import os
os.system("cls")

# MANEJO DE FICHEROS

# - .txt -

txt_file = open("Intermedio/my_file.txt", "r+")  # r+ lee y escribe
# print(txt_file.read())
# print(txt_file.read(10))
print(txt_file.readlines())
# print(txt_file.readline())