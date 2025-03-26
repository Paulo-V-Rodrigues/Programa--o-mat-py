# Solicita os valores das contas e do salário ao usuário
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))
conta3 = float(input("Digite o valor da terceira conta: "))
salario = float(input("Digite o valor do seu salário: "))

# Calcula o total das contas
total_contas = conta1 + conta2 + conta3

# Verifica se o salário é suficiente para pagar as contas
if salario >= total_contas:
    restante = salario - total_contas
    print(f"Salário suficiente! O valor restante é: R$ {restante:.2f}")
else:
    print("Salário insuficiente!")
