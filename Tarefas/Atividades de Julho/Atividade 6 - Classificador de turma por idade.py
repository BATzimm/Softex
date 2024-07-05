idades = []
idade = int(input("Digite a idade (0 para sair): "))

while idade != 0:
    idades.append(idade)
    idade = int(input("Digite a idade (0 para sair): "))

media_idade = sum(idades) // len(idades)  # Usando divisão inteira para obter um resultado sem casas decimais

if media_idade <= 25:
    classificacao = "Jovem"
elif media_idade <= 60:
    classificacao = "Adulta"
else:
    classificacao = "Idosa"

print(f"A média de idade da turma é {media_idade} anos.")  # Sem casas decimais
print(f"A turma é classificada como {classificacao}.")
