def converter_numero():
    try:
        numero_decimal = int(input("Digite um número decimal: "))
        print("Escolha a base para conversão:")
        print("1 - Binário")
        print("2 - Octal")
        print("3 - Hexadecimal")
        base = int(input("Digite o número correspondente à base escolhida: "))

        if base == 1:
            print(f"O número {numero_decimal} em binário é: {bin(numero_decimal)[2:]}")
        elif base == 2:
            print(f"O número {numero_decimal} em octal é: {oct(numero_decimal)[2:]}")
        elif base == 3:
            print(f"O número {numero_decimal} em hexadecimal é: {hex(numero_decimal)[2:]}")
        else:
            print("Base inválida. Escolha 1, 2 ou 3.")
    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    while True:
        converter_numero()
        continuar = input("Deseja converter outro número? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa. Até mais!")
            break