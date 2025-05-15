nomes = []
notas = []

n = int(input('Digite a quantidade de alunos:'))

for i in range(n):
    nome = input(f'Digite o nome do {i+1} aluno: ').capitalize()
    nomes.append(nome)
    nota = float(input(f'Digite a nota do {nome}:'))
    notas.append(nota)

media_turma= sum(notas)/len(notas)
print(f'Media da turma: {media_turma:.2f}')

for i in range(n):
    if notas[i] > media_turma:
        print(f'Parabens {nomes[1]}!')