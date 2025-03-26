salary = float(input('Digite o seu salário: R$'))

comission = salary * 0.05 

salaryWithComission = comission + salary

print(f'O seu salário é R${salary:.2f}, o seu acréscimo de 5% de comissão é de R${comission:.2f}, totalizando um salário de R${salaryWithComission:.2f}')