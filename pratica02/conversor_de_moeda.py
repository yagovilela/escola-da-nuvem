# Conversor de Moeda 
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.60
# Taxa do euro: R$ 6.60 
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

print("Conversor de Moeda")

valor_real = 100
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_real / taxa_dolar
valor_euro = valor_real / taxa_euro

print(f'Valor em reais: R$ {valor_real: .2f}')
print(f'Valor em dolar: U$$ {valor_dolar: .2f}')
print(f'Valor em euro: £ {valor_euro: .2f}')