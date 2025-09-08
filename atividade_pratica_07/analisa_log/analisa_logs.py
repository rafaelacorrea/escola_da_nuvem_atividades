import re
import statistics

def analisar_logs(caminho_arquivo):
    tempos = []

    padrao = re.compile(r"tempo:\s*([0-9]*\.?[0-9]+)")

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            match = padrao.search(linha)
            if match:
                tempos.append(float(match.group(1)))

    if tempos:
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0

        print("=== Estatísticas do Treinamento ===")
        print(f"Quantidade de registros: {len(tempos)}")
        print(f"Média do tempo de execução: {media:.4f}")
        print(f"Desvio padrão: {desvio:.4f}")
    else:
        print("Nenhum dado de tempo encontrado no arquivo.")

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo de log: ")
    analisar_logs(caminho)
