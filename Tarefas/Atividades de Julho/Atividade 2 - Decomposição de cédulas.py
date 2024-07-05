cedulas = [100, 50, 20, 10, 5, 2, 1]

def decompose_cedulas(valor):
    quantidade_cedulas = []

    for cedula in cedulas:
        quantidade = valor // cedula
        valor %= cedula
        quantidade_cedulas.append(int(quantidade))  # Convertendo para int para garantir números inteiros

    return quantidade_cedulas

valor = float(input("Digite o valor em reais: "))
quantidade_cedulas = decompose_cedulas(valor)

print("Quantidade mínima de cédulas:")
for i in range(len(quantidade_cedulas)):
    if quantidade_cedulas[i] > 0:
        print(f"{quantidade_cedulas[i]} cédula(s) de R$ {cedulas[i]}")