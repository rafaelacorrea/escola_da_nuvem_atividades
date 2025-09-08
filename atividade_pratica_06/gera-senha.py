import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    qtd = int(input("Digite a quantidade de caracteres da senha: "))
    if qtd <= 0:
        print("A quantidade de caracteres deve ser maior que zero.")
    else:
        senha_gerada = gerar_senha(qtd)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número válido.")
