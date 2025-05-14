num = []

while True:
    n = int(input('Digite um numero'))
    if n == 0: break
    num.append(n)

print(num)
media = sum(num)/len(n)
print(f'media {media:.2f}')