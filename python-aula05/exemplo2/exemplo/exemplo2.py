media = float(input('digite sua senha'))
freq = int(input('Digite a sua fraquencia'))

if freq < 75:
    print('Reprovado por falta')
elif media < 3:
    print('Reprovado por nota')
elif media < 6:
    print('Avaliação final')
else:
    print('Aprovado')