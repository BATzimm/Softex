
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votos_nulos = 0
votos_em_branco = 0

while True:
    print("Digite o número do candidato que deseja votar (1, 2, 3 ou 4), ou digite 0 para encerrar a votação:")
    voto = int(input())

    # Verificando se o voto é válido
    if voto == 0:
        break
    elif voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    else:
        votos_nulos += 1

total_votos = candidato1 + candidato2 + candidato3 + candidato4 + votos_nulos

porcentagem_candidato1 = (candidato1 / total_votos) * 100
porcentagem_candidato2 = (candidato2 / total_votos) * 100
porcentagem_candidato3 = (candidato3 / total_votos) * 100
porcentagem_candidato4 = (candidato4 / total_votos) * 100
porcentagem_votos_nulos = (votos_nulos / total_votos) * 100
porcentagem_votos_em_branco = (votos_em_branco / total_votos) * 100

print("Total de votos para o candidato 1:", candidato1)
print("Total de votos para o candidato 2:", candidato2)
print("Total de votos para o candidato 3:", candidato3)
print("Total de votos para o candidato 4:", candidato4)
print("Total de votos nulos:", votos_nulos)
print("Total de votos em branco:", votos_em_branco)
print("Porcentagem de votos para o candidato 1:", porcentagem_candidato1, "%")
print("Porcentagem de votos para o candidato 2:", porcentagem_candidato2, "%")
print("Porcentagem de votos para o candidato 3:", porcentagem_candidato3, "%")
print("Porcentagem de votos para o candidato 4:", porcentagem_candidato4, "%")
print("Porcentagem de votos nulos:", porcentagem_votos_nulos, "%")
print("Porcentagem de votos em branco:", porcentagem_votos_em_branco, "%")