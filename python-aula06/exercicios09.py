import os
os.system('cls')

print(' Digite 1 para media entre os numeros digitados')
print(' Digite 2 para diferença entre os numeros digitados')
print(' Digite 3 para o maior numero digitado')
print(' Digite 4 para o menor numero digitado')

op = int(input('Digite a opcao desejada: '))

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

match op:
    case 1:
        media = (n1 + n2) / 2
        print(f'A media entre {n1} e {n2} é {media}')
    case 2:
        soma = n1 + n2
        print(f'A diferença entre {n1} e {n2} é {soma}')
    case 3:
        if n1 > n2:
            print(f'Produto entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior numero entre {n1} e {n2} é {n2}')
    case 4:
        if n1 < n2:
            print(f'Divisão entre {n1} e {n2} é {n1}')
        else:
            print(f'O menor numero entre {n1} e {n2} é {n2}')
    case _:
        print('Opcao invalida')