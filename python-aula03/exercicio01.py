import math
x1 = float(input('Digite a coordenada X1 :'))
y1 = float(input('Digite a coordenada Y1 :'))

x2 = float(input('Digite a coordenada X2 :'))
y2 = float(input('Digite a coordenada Y2 :'))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'A distância entre os pontos é {d:.2f}')
