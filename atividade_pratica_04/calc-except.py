while True:
    print("\nCalculadora - Operações Básicas (+, -, *, /)")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        resultado = 0

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':

            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue 
            resultado = num1 / num2
        else:

            print("Erro: Operação inválida. Por favor, use +, -, * ou /.")
            continue  
            
        print(f"\nO resultado da operação é: {resultado}")
        break  
        
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")