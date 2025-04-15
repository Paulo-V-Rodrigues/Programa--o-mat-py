contador = 0
soma = 0
resp = 's'

while resp in 'sS':
    num = int(input(f'digite o {contador+1}º número:'))
    soma += num
    contador += 1
    
    
    resp= input('deseja continuar? Si/No:')
    
    
    media = soma/contador
    print(f'A média dos números é {media:.2f}')
