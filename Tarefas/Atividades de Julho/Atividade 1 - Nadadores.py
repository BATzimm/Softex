
idade = int(input("Bem-vindo a inscrição de competição de natação. Insira sua idade: "))
if idade < 5:
    print("Idade mínima para participação é de 5 anos.")

elif idade >= 5 or idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 or idade <= 11:
    print("Categoria: Infantil B")
elif idade >= 12 or idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 or idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18 or idade <= 59:
    print("Categoria: Adulto")
elif idade <= 60:
    print("Por favor, busque outra competição.")
else:
    print("Dados inválidos. Insira a idade do participante")

