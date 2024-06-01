import os
os.system("cls")

# =========
# = FECHAS =
# =========

import datetime

now = datetime.datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.second)
print(now.minute)
print(now.hour)

timestamp = now.timestamp()  # <- este es un formato estandar para horarios
print(timestamp)



def print_date(date):       # <- aqui definimos una funcion que imprima los distintos tipos de horario
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.second)
    print(date.minute)
    print(date.hour)
    print(date.timestamp())

print_date(now)


year_2025 = datetime.datetime(2025, 1, 1) # <- aqui creamos una variable para almacenar los datos segun nuestros parametros
print_date(year_2025) # <- aqui evaluamos la funcion segun los parametros de arriba

from datetime import time  # <- time es solo para horarios

current_time = time(23,24,2)
current_time.hour

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime  import date  # <- date es solo para fechas

current_date = date(2024,6,27)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month +1 , current_date.day)

print(current_date)

diff = year_2025 - now
print(diff)
print(year_2025.date() - current_date)


from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
