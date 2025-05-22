import hipotenusa

catO = float(input("Digite o cateto oposto: "))
catA = float(input("Digite o cateto adjacente: "))
print(f'Seno: {hipotenusa.seno(catO, catA)}')
print(f'Seno: {hipotenusa.cosseno(catO, catA)}')
print(f'Seno: {hipotenusa.tangente(catO, catA)}')