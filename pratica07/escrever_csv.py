"""Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade."""

import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)   # usa csv.writer
            escritor.writerow(['Nome', 'Idade', 'Cidade'])  # cabeçalho
            for linha in dados:
                escritor.writerow(linha)
        print(f"Arquivo {nome_arquivo} salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Lista de dados (note as vírgulas entre as listas)
dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Bernardo', 30, 'São Paulo'],
    ['Carlos', 29, 'Belo Horizonte'],
    ['Maria', 32, 'Salvador']
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()  # precisa dos ()
    escrever_csv(nome_arquivo, dados)
