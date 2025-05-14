notas = [6, 7, 6.5, 4.8, 8]

soma = 0
for nota in notas:
    soma += nota
media = soma/5
print(f'A media do aluno é: {media:.2f}!')

quantos = 0
for nota in notas:
    if nota > media:
        quantos += 1
print(f'exitem {quantos} notas acima da media {media:.2f}')