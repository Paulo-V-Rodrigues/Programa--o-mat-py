cliente_mais_alto = 0
altura_mais_alta = 0
soma_pesos = 0
quantidade_clientes = 0

while True:
    codigo = input("Digite o seu código de acesso (ou pressione ENTER para encerrar): ")
    if codigo == "":
        break
    
    altura = float(input("Digite a sua altura (em metros): "))
    peso = float(input("Digite o seu peso (em kg): "))
    
    if altura > altura_mais_alta:
        altura_mais_alta = altura
        cliente_mais_alto = codigo

    soma_pesos += peso
    quantidade_clientes += 1

if quantidade_clientes > 0:
    media_pesos = soma_pesos / quantidade_clientes
else:
    media_pesos = 0

print(f"O cliente mais alto é o de código {cliente_mais_alto} com altura de {altura_mais_alta:.2f} metros.")
print(f"A média dos pesos dos clientes é {media_pesos:.2f} kg.")
print(f"O codigo do maior aluno é: {cliente_mais_alto}")