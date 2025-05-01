import random

ganho = 0
aposta = 0

while True:
    bola1 = 'Preta' if random.randint(0, 1) == 0 else 'Vermelha'
    bola2 = 'Preta' if random.randint(0, 1) == 0 else 'Vermelha'
    aposta = float(input('Qual o valor da aposta? '))
    
    print(f'As bolas sorteadas foram: {bola1} e {bola2}')
    if bola1 == 'Preta' and bola2 == 'Preta':
        ganho += aposta * 2
    elif bola1 == 'Vermelha' and bola2 == 'Vermelha':
        ganho += 0
    elif bola1 == 'Preta' and bola2 == 'Vermelha':
        ganho += aposta
    else:
        ganho += aposta/2
    print(f'Você ganhou: {ganho}')
    aposta += aposta
    ganho += ganho
    if (input('deseja continuar? [s/n]: ') in 'nN'):
        break
    lucro = ganho - aposta
print(f'Você teve um lucro de {aposta}')
print(f'Você teve um ganha de {lucro:.2f} reais')