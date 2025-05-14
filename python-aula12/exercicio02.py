nome = []

for i in range(5):
    nome = input(f'Digite o nome de 5 {i+1} pessoas').capitalize()
    nome.append(nome)
print(nome)
n = int(input('Digite um numero entre 0 e 4:'))

while n < 0 or n > len(nome):
    print('presta atenção na perguntar!!')
    n = int(input('Digite um numero de 0 até 4'))

print('Não encontrado')