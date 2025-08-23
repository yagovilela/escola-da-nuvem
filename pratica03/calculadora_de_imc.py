# Calculadora de IMC
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
# < 18.5: classificacao = "Abaixo do peso" 
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"



print("Calculadora de IMC")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Fórmula do IMC: peso / (altura^2)
imc = peso / (altura ** 2)

# Classificação de acordo com a tabela
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")
