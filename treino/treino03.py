contador = 1
while contador <= 10:
    n1 = float(input(f'Digite a primeira nota: '))
    n2 = float(input(f'Digite a segunda nota: '))
    n3 = float(input(f'Digite a terceira nota: '))
    n4 = float(input(f'Digite a quarta nota: '))
    media = (n1 + n2 + n3 + n4)/2
    print(f'A média é {media}')
    contador = contador +1