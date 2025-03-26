def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta >= 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        
        return x1, x2
    else:
        return None

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("O coeficiente 'a' não pode ser zero.")
else:
    raizes = calcular_raizes(a, b, c)
    
    if raizes:
        print(f"As raízes da equação são: x1 = {raizes[0]} e x2 = {raizes[1]}")
    else:
        print("A equação não tem raízes reais.")
