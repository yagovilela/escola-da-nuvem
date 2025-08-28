"""Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

while True:
    try:
        preco = float(input("Insira o preço do produto(R$): "))
        percentual_desconto = float(input("Insira o percentual de desnconto(%): "))
        break
    
    except ValueError:
        print("Por favor, insira um valor númerico.")

preco_com_desconto = calcular_desconto(preco, percentual_desconto)
print(f"O preço final com desconto de {percentual_desconto}% é: R$ {preco_com_desconto:.2f}")
                    