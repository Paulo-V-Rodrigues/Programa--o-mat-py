contador = 0
altura = 3
soma = 0

while altura > 0:
    altura = float(input(f'digite o {contador+1}º altura: '))
    soma += altura
    contador +=1
    
    
media = soma / contador
print(f'A média das alturas é {media:.2f}')