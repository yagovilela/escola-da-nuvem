# Calculadora de Desconto 
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

print('Calculadora de Desconto')

nome_produto = 'Camiseta'
preco_original = 50.00
valor_desconto = 20 / 100
preco_com_desconto = preco_original * valor_desconto
valor_final = preco_original - preco_com_desconto

print('Produto:',nome_produto)
print(f'Valor do produto: R$ {preco_original: .2f}')
print(f'Valor do desconto: R$ {preco_com_desconto: .2f}')
print (f'Valor final do produto: R$ {valor_final}')
