capacidade_tanque = 40

quilometragem = float(input("Digite a quilometragem rodada desde o último abastecimento (km): "))
consumo_medio = float(input("Digite o consumo médio do veículo (km/L): "))

combustivel_utilizado = quilometragem / consumo_medio

combustivel_restante = capacidade_tanque - combustivel_utilizado
porcentagem_restante = (combustivel_restante / capacidade_tanque) * 100

if porcentagem_restante < 25:
    print(f"Atenção: O nível de combustível está baixo ({porcentagem_restante:.2f}%). Por favor, abasteça!")
else:
    print(f"O nível de combustível está adequado ({porcentagem_restante:.2f}%).")

if combustivel_restante < 0:
    print("Você rodou mais do que o possível com o combustível disponível. Abasteça imediatamente!")
