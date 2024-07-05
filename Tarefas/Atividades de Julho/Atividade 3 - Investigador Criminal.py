

def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (s/n): ")
    return resposta.lower() == "s"

def contar_respostas_positivas(respostas):
    contador = 0
    for resposta in respostas:
        if resposta:
            contador += 1
    return contador

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = fazer_pergunta(pergunta)
    respostas.append(resposta)

num_respostas_positivas = contar_respostas_positivas(respostas)

if num_respostas_positivas == 0 or num_respostas_positivas == 1:
    classificacao = "Inocente"
elif num_respostas_positivas == 2:
    classificacao = "Suspeito"
elif num_respostas_positivas == 3 or num_respostas_positivas == 4:
    classificacao = "Cúmplice"
else:
    classificacao = "Assassino"

print("Você é: " + classificacao)