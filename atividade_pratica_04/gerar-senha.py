while True:
    senha = input("Digite sua senha (mínimo 8 caracteres e 1 número) ou 'sair' para terminar: ")
    
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    if len(senha) < 8:
        print("Sua senha é muito curta. Ela deve ter pelo menos 8 caracteres.")
        continue

    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break
            
    if not tem_numero:
        print("Sua senha deve conter pelo menos um número.")
        continue

    print("Senha forte e válida. Acesso concedido!")
    break