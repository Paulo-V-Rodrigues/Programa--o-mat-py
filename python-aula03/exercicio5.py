import math

graus = int(input('Digite o valor do angulo em graus: '))

radianos = math.radians(graus)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'Radianos: {radianos:.2f}. Seno: {seno:.2f}. Cosseno: {cosseno:.2f}. Tangente: {tangente:.2f}')

