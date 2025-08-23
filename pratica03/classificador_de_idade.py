# Classificador de Idade
# Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:
# Criança (0-12 anos),
# Adolescente (13-17 anos),
# Adulto (18-59 anos),
# Idoso (60 anos ou mais).

print("Classificador de Idade")

# Entrada
idade = int(input("Digite sua idade: "))

# Saída
if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 15:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
elif 60 <= idade <= 105:
    print("Idoso")
elif idade >= 106:
    print("Idade Inválida")