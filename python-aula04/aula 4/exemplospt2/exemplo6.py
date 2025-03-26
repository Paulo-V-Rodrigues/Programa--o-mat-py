# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica se o valor ultrapassa R$ 100,00 para aplicar o desconto
if valor_compra > 100:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 5% (R$ {desconto:.2f}).")
else:
    valor_final = valor_compra

print(f"O valor total a ser pago é: R$ {valor_final:.2f}")
