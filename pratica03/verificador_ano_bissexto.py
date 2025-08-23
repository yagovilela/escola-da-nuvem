# Verificador de Ano Bissexto
# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

print("Verificador de Ano Bissexto")

ano = int(input("Digite um ano: "))

# Regra do ano bissexto:
# - Divisível por 4 E (não divisível por 100 OU divisível por 400)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")