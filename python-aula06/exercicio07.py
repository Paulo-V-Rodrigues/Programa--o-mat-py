import os
os.system('cls')

cordenadasx = float(input('Digite a cordenada x: '))
cordenadasy = float(input('Digite a cordenada y: '))

if cordenadasx > 0 and cordenadasy > 0:
    print('Primeiro quadrante')
elif cordenadasx < 0 and cordenadasy > 0:
    print('Segundo quadrante')
elif cordenadasx < 0 and cordenadasy < 0:
    print('Terceiro quadrante')
elif cordenadasx > 0 and cordenadasy < 0:
    print('Quarto quadrante')
else:
    print(f'O ponto p({cordenadasx},{cordenadasy}) pertence ao {quadrante} quadrante')