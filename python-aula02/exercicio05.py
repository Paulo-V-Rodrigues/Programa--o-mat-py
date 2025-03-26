cotacao = float(input('Digite a cotação do dólar: '))
dolar = float(input('Digite um valor em dólar: '))

reais = dolar * cotacao

print(f'O valor de {dolar}USD é de R${reais:.2f}')