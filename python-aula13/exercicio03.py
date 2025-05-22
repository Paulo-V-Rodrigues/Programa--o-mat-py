import os
os.system('cls')

n1 = int(input(f'Digite um numero '))
n2 = int(input(f'Digite um numero '))

media = (n1+n2)/2

print(f'A media é {media}')

#
def media(a, b):
    media = (a*2+b*5)/7
    print(f'A media é {media}')

n1 = int(input(f'Digite um numero '))
n2 = int(input(f'Digite um numero '))
media(n1, n2)
media(8,9)
media(10, 16)
media(5, 8)