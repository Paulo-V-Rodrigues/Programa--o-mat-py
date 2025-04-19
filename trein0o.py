import os
os.system('cls')

altura = float(input("Digite a altura da pessoa: "))
sexo = input("Digite o seu sexo M ou F: ")
if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
    exit()
print(f'O peso ideal para uma pessoa do sexo {sexo} com altura {altura} é {peso_ideal:.2f} kg')