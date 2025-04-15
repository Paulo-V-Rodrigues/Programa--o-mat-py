maior = 1
i = 1
while i <=10:
    nome = input('digite o nome do aluno:')
    nota1 = float(input('digite a primeira nota do aluno:'))
    nota2 = float(input('digite a segunda nota do aluno:'))
    
    media = (nota1 + nota2)/ 2
    if media > maior:
        maior = media
    print(f'A maior média {nome} é {media:.2f}')
    
    i+=1
    
    print(f'a maior média é {maior}')