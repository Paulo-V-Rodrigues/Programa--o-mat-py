import os
os.system('cls')

segundos = int(input('Digite a quantidade de segundos: '))
horas = segundos // 3600
minutos = segundos % 3600 // 60
segundos = segundos % 60

print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')