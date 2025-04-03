import os
os.system('cls')

n1 = int(input('Digite o primeira nota: '))
n2 = int(input('Digite o segunda nota: '))

media = (n1 + n2) / 2

if media >= 9.0 and media <= 10.0:
    print('Aprovado com A')
elif media >= 7.5 and media < 8.9:
    print('Aprovado com B')
elif media >= 6.0 and media < 7.4:
    print('Aprovado com C')
elif media <= 4.0 and media < 5.9:
    print('Reprovado com D')
else:
    print('Reprovado com E')