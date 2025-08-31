pares = 0
impares = 0

print("Digite números inteiros. O programa irá informar se são pares ou ímpares.")
print("Para terminar, digite 'fim'.")

while True:
    entrada = input("\nDigite um número inteiro: ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        numero = int(entrada)
        
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
            
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("\n--- Resumo ---")
print(f"Total de números pares inseridos: {pares}")
print(f"Total de números ímpares inseridos: {impares}")