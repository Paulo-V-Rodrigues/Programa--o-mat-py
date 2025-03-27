def exibir_tabela_precos():
    print("Tabela de Preços:")
    print("1 - Econômica: R$ 255,50 por diária")
    print("2 - Executiva: R$ 305,50 por diária")
    print("3 - Luxo: R$ 360,50 por diária")
    print()

def calcular_valor_total(codigo, quantidade):
    if codigo == 1:
        return quantidade * 255,50
    elif codigo == 2:
        return quantidade * 305,50
    elif codigo == 3:
        return quantidade * 360,50
    else:
        return None

def main():
    exibir_tabela_precos()
    
    try:
        codigo = int(input("Digite o código do tipo de diária (1, 2 ou 3): "))
        quantidade = int(input("Digite a quantidade de diárias desejadas: "))
        
        valor_total = calcular_valor_total(codigo, quantidade)
        
        if valor_total is not None:
            print(f"O valor total a pagar é: R$ {valor_total:.2f}")
        else:
            print("Código inválido. Por favor, tente novamente.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números inteiros.")

if __name__ == "__main__":
    main()