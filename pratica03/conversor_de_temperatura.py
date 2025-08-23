# Conversor de Temperatura 
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# Programa: Conversor de Temperatura

print("=== Conversor de Temperatura ===")
temp = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F ou K): ").upper()
destino = input("Informe a unidade de destino (C, F ou K): ").upper()

# Primeiro, vamos converter tudo para Celsius
if origem == "C":
    celsius = temp
elif origem == "F":
    celsius = (temp - 32) * 5/9
elif origem == "K":
    celsius = temp - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Agora converte do Celsius para o destino
if destino == "C":
    convertido = celsius
elif destino == "F":
    convertido = (celsius * 9/5) + 32
elif destino == "K":
    convertido = celsius + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"{temp:.2f} {origem} = {convertido:.2f} {destino}")