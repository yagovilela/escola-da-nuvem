"""Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação."""

import requests

def consultar_cotacao():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()

    # Monta a URL: cotação da moeda informada em relação ao BRL
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()

            # A chave do retorno é algo como "USDBRL", "EURBRL", etc.
            chave = f"{moeda}BRL"
            if chave in dados:
                info = dados[chave]
                valor = info.get("bid")
                maximo = info.get("high")
                minimo = info.get("low")
                data_hora = info.get("create_date") or f"{info.get('create_date', 'N/A')}"

                print("\n=== Cotação Atual ===")
                print(f"Moeda: {moeda}/BRL")
                print(f"Valor atual: R$ {valor}")
                print(f"Máximo do dia: R$ {maximo}")
                print(f"Mínimo do dia: R$ {minimo}")
                print(f"Última atualização: {data_hora}")
            else:
                print("Não foi possível encontrar informações para essa moeda.")
        else:
            print("Erro ao acessar a API. Código:", resposta.status_code)

    except requests.exceptions.RequestException as e:
        print("Erro de conexão:", e)

# Executa o programa
consultar_cotacao()
