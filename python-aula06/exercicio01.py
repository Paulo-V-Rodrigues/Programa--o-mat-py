import os
os.system("cls")

salariofixo = float(input("Digite o salário fixo: R$ "))
valorvendas = float(input("Digite o valor total das vendas: R$ "))

comissao = valorvendas * 4/100
salariototal = salariofixo + comissao

print(f"O salário total é de R${salariototal:.2f}")
print(f"O salário fixo é de R${salariofixo:.2f}")
print(f"A comissão é de R${comissao:.2f}")