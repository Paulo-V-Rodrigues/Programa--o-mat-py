soma = 0

for i in range(10):
    num = float(input(f'digite o {i+1}º número:'))
    soma = soma + num # ou soma += num
    
    print(f'a soma dos números digitados é {soma}')