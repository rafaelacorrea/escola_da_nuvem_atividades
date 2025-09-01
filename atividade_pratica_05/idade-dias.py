from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    data_nascimento = date(ano_nascimento, 1, 1)
    
    data_atual = date.today()

    diferenca = data_atual - data_nascimento

    return diferenca.days

try:
    ano = int(input("Digite o ano de nascimento (ex: 1990): "))

    if ano > date.today().year or ano < 1900:
        print("Ano de nascimento inválido.")
    else:
        idade_em_dias = calcular_idade_em_dias(ano)
        print(f"Uma pessoa nascida em {ano} tem aproximadamente {idade_em_dias} dias de idade.")
        
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para o ano.")