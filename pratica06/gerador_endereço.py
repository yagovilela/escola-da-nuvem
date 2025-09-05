"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""

import requests

def consultar_cep():
    cep = input("Digite o CEP (somente números): ").strip()

    # Monta a URL da API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()

            # Verifica se o CEP é inválido
            if "erro" in dados:
                print("CEP não encontrado.")
            else:
                print("=== Endereço encontrado ===")
                print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
                print(f"Bairro: {dados.get('bairro', 'N/A')}")
                print(f"Cidade: {dados.get('localidade', 'N/A')}")
                print(f"Estado: {dados.get('uf', 'N/A')}")
        else:
            print("Erro ao consultar a API. Código:", resposta.status_code)

    except requests.exceptions.RequestException as e:
        print("Erro de conexão:", e)

# executa o programa
consultar_cep()
