print('Hospedagem analia\n[s]imples\n[d]uplo\n[t]riplo\n[q]uadruplo\n')
opc = input('Digite o tipo de hospedagem: ')
dias = int(input('Digite a quantidade de dias: '))
if opc not in 'sdqt':
    print('opção inválida')
else:
    diarias = int(input('Digite a quantidade de diárias: '))
if opc == 's':
    valor = 255,50
elif opc == 'd':
    valor = 305,50
elif opc == 't':
    valor = 360,50
else:
    print(f'O valor total a pagar é: R$ {total:.2f}')