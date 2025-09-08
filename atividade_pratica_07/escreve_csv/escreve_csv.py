import csv

def escrever_csv(nome_arquivo):
    pessoas = [
        {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Bruno", "Idade": 34, "Cidade": "Rio de Janeiro"},
        {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"},
    ]

    colunas = ["Nome", "Idade", "Cidade"]

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)

        escritor.writeheader()
        escritor.writerows(pessoas)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

if __name__ == "__main__":
    escrever_csv("dados_pessoais.csv")
