def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0
    
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    
    return valor_gorjeta

valor_da_conta = int(input("Digite o valor da sua conta: "))
porcentagem_desejada = int(input("Digite o valor da porcentagem desejada: "))

gorjeta_calculada = calcular_gorjeta(valor_da_conta, porcentagem_desejada)

print(f"O valor da conta é: R${valor_da_conta:.2f}")
print(f"A porcentagem de gorjeta desejada é: {porcentagem_desejada}%")
print(f"O valor da gorjeta a ser deixada é: R${gorjeta_calculada:.2f}")