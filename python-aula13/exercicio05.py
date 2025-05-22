def calculaArea(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Digite a base do triângulo (em cm): "))
altura = float(input("Digite a altura do triângulo (em cm): "))

area = calculaArea(base, altura)

print(f"A área do triângulo é: {area:.2f} cm")