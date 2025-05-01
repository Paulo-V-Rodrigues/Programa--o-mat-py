cont = 0

tel = input("Telefonou para a vítima? [s/n]: ").strip().lower()
if tel == 's':
    cont += 1

local = input("Esteve no local do crime? [s/n]: ").strip().lower()
if local == 's':
    cont += 1

mora = input("Mora perto da vítima? [s/n]: ").strip().lower()
if mora == 's':
    cont += 1

devia = input("Devia para a vítima? [s/n]: ").strip().lower()
if devia == 's':
    cont += 1

tab = input("Já trabalhou com a vítima? [s/n]: ").strip().lower()
if tab == 's':
    cont += 1

if cont == 2:
    print("Classificação: Suspeito")
elif 3 <= cont <= 4:
    print("Classificação: Cúmplice")
elif cont == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")