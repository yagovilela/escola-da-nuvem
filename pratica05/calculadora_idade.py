"""Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year # Coleta o ano atual do sistema
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Insira o ano do seu nascimento: "))
dias = idade_em_dias(ano_nascimento)

print(f"O ano que nasceu foi {ano_nascimento}, com isso voce tem aproximadamente {dias} dias")