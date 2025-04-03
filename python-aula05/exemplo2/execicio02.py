import os
os.system('cls')

valores = {'s': 255.50, 'd': 305.50, 't': 360.50}
tip = input('Digite o tipo de diaria (S/D/T): ').lower()
quantidade = int(input('Digite a quantidade de diarias: '))

if tip in valores:
    total = valores[tip] * quantidade
    print(f'O valor total da diária é: R$ {total:.2f}')
else:
    print('A diária informada é inválida!')