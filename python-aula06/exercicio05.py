import os
import math

os.system("cls")

tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = tamanho_area / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total = latas_necessarias * 80
if latas_necessarias > 1:
    print(f"Serão necessárias {latas_necessarias} latas de tinta, totalizando R${preco_total:.2f}")