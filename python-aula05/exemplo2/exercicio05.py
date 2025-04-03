compra = float(input("Digite o valor da compra: "))
parcelas = int(input('Digite a quantidade de parcelas (2, 4, 6 ou 8)'))

match(parcelas):
    case 2: valor = parcelas * 1.03
    case 4: valor = parcelas * 1.07
    case 6: valor = parcelas * 1.09
    case 8: valor = parcelas * 1.12
    case _: valor = 0

if valor == 0:
    print('Quantidade de parcelas inválida!!!')
else:
    print(f'Valor de cada parcela: {valor/parcelas}')