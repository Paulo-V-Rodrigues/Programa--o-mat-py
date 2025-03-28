import os
os.system

media = float(input('Digite a sua média: '))
freq = int(input('Digite a sua frequência: '))

if freq < 75:
    print('Reprovado por falta')
elif media < 3:
    print('Reprovado por nota')
elif media < 6:
    print('Avaliação final')
else:
    print('Aprovado')