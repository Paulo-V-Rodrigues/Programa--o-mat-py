try:
    conta = int(input('Digite o Numero da conta com até 4 digitos:'))

    if not (conta >= 1000 and conta <= 9999):
        print('Número de conta inválido')
    else:
        soma_digitos = sum(int(digito) for digito in str(conta))
        print(f"A soma dos dígitos de {conta} é: {soma_digitos}")
except ValueError:
    print("Erro: Digite apenas números.")
