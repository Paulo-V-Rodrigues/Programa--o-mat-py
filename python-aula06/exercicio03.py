import os
os.system('cls')

num = (int(input("Digite um número inteiro: ")))
if num > 0:
    res = 'positivo'
elif num < 0:
    res = 'negativo'
else:
    res = 'nulo'
print(f"O número {num} é {res}.")