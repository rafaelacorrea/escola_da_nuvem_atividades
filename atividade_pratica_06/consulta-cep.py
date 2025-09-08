import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "erro" in dados:
            print("❌ CEP não encontrado.")
        else:
            print("=== Endereço encontrado ===")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")
    else:
        print("❌ Erro ao acessar a API.")

cep = input("Digite o CEP (somente números): ").strip()
consultar_cep(cep)
