import json

def escrever_json(nome_arquivo):
    pessoa = {
        "nome": "Ana",
        "idade": 28,
        "cidade": "São Paulo"
    }

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            pessoa = json.load(arquivo)

        print("\n=== Dados do Arquivo JSON ===")
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Cidade: {pessoa['cidade']}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    nome_arquivo = "pessoa.json"
    escrever_json(nome_arquivo)
    ler_json(nome_arquivo)
