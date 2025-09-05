"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória."""

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    quantidade = int(input("Insira a quantidade de caracteres da senha: "))
    if quantidade < 4:
        print("A senha deve ter pelo menos 4 caracteres.")
    else:
        senha = gerar_senha(quantidade)
        print(f"Sua senha é: {senha}")

except ValueError:
    print("Por favor, digite um número inteiro válido.")