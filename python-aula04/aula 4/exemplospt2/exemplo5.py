# Solicita a placa do veículo
placa = input("Digite a placa do veículo: ")

# Solicita o número de horas estacionadas
horas = int(input("Digite o número de horas estacionadas: "))

# Calcula o valor a ser pago
if horas <= 2:
    valor = 5.00
else:
    valor = 10.00

# Exibe o valor a ser pago
print(f"Veículo com placa {placa} deve pagar R$ {valor:.2f}.")
