valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra > 200:
    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 20% nas compra acima de $200. Valor final da compra: R$ {valor_final:.2f}")
else:
    print(f"Não há desconto apenas compras acima de R$ 200 a loja dá um desconto de 20% no Valor final da compra: Valor da compra R$ {valor_compra:.2f}")
