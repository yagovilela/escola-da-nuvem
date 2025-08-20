# Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
# Distância percorrida: 300 km
# Combustível gasto: 25 litros 
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

distancia_percorrida = 300
combustivel_gasto = 25

consumo = distancia_percorrida / combustivel_gasto

print('Dados da Viagem:')
print('Distancia percorrida: ', distancia_percorrida , 'km')
print('Combustivel gasto: ', combustivel_gasto,'l')

print(f'Consumo médio: {consumo:.2f} km/l')