notas = []

print("Bem-vindo! Digite as notas dos alunos. Digite 'fim' para encerrar.")

while True:
    entrada = input("Digite a nota (0-10) ou 'fim' para terminar: ")

    if entrada.lower() == 'fim':
        break
        
    try:
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("A nota deve ser entre 0 e 10. Por favor, tente novamente.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\n--- Resultado ---\nTotal de notas válidas inseridas: {len(notas)}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi inserida.")