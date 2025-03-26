import math

n = int(input('Digite o número de lados do polígono: '))
s = float(input('Digite o comprimento de cada lado do polígono: '))

a =( n*s**2) / (4 * math.tan(math.pi / n))

print(f'A área do polígono é {a:.2f}')