n = int(input("Digite a quantidade de números da série de Fibonacci que deseja ver: "))

fibonacci = [0, 1]

for i in range(2, n):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)

print("Série de Fibonacci:")
print(fibonacci[:n])