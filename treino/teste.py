try:
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    
    # Validação de altura razoável
    if altura <= 0 or altura > 2.5:
        print("Altura inválida. Por favor, insira a altura em metros, como por exemplo 1.75.")
        exit()

    sexo = input("Digite seu sexo (M para masculino ou F para feminino): ").strip().lower()

    if sexo == 'm':
        peso_ideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    elif sexo == 'f':
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    else:
        print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")

except ValueError:
    print("Entrada inválida. Certifique-se de digitar a altura como um número, usando ponto (.) e não vírgula (,).")
