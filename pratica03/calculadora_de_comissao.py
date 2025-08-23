# Calculadora de Comissão
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
# Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente. 
# Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

print("Calculadora de Comissão")

# Entrada de dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = float(input("Digite o total de vendas: R$ "))

# Cálculo da comissão (15%)
comissao = total_vendas * 0.15

# Salário final
salario_total = salario_fixo + comissao

# Saída formatada
print(f"O vendedor {nome} deverá receber R$ {salario_total:.2f} no final do mês.")
