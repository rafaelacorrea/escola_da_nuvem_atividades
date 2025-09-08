import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            print("=== Dados do Arquivo CSV ===")
            for linha in leitor:
                nome = linha["Nome"]
                idade = linha["Idade"]
                cidade = linha["Cidade"]
                print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    ler_csv("dados_pessoais.csv")
