import os
os.system('cls')

valor = float(input('Digite o valor da compra: '))
parcelas = int(input('Digite o número de parcelas (2, 4, 6, 8): '))

# Definindo os juros para cada número de parcelas
if parcelas == 2:
    juros = 0.03  # 2% de juros
elif parcelas == 4:
    juros = 0.07  # 4% de juros
elif parcelas == 6:
    juros = 0.09  # 6% de juros
elif parcelas == 8:
    juros = 0.12  # 8% de juros
else:
    juros = None  # Número de parcelas inválido

if juros is not None:
    valor_total = valor * (1 + juros)  # Aplicando os juros ao valor total
    valor_parcela = valor_total / parcelas
    print(f'O valor total com juros é: R$ {valor_total:.2f}')
    print(f'O valor de cada parcela é: R$ {valor_parcela:.2f}')
else:
    print('Número de parcelas inválido!')
    print('O número de parcelas deve ser 2, 4, 6 ou 8.')