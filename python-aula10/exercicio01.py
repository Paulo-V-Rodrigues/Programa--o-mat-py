import os
os.system('cls')
soma = 0

num = int(input('Digite os 4 digitos de segurança do cartão:(0000) '))

for n in num:
    soma += int(n)

dig = soma % 10
print(f'O Numero segurança cartão é: 00{int(num):06d}-{dig}')