valorPrestacao = float(input('Digite o valor da prestação: R$'))
multa = float(input('Digite a porcentagem de multa: '))
qtdeDias = int(input('Digite a quantidade de dias de atraso: '))


prestacao = valorPrestacao + (valorPrestacao * (multa/100) * qtdeDias)


print(f'O valor atualizado da prestação é: R${prestacao:.2f}')