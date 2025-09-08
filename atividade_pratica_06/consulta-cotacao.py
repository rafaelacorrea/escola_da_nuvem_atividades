import requests

def consultar_cotacao():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]
            print("\n=== Cotação Atual ===")
            print(f"Moeda: {cotacao['code']} -> {cotacao['codein']}")
            print(f"Valor atual: R$ {cotacao['bid']}")
            print(f"Valor máximo: R$ {cotacao['high']}")
            print(f"Valor mínimo: R$ {cotacao['low']}")
            print(f"Última atualização: {cotacao['create_date']}")
        else:
            print("Moeda não encontrada. Verifique o código informado.")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    consultar_cotacao()