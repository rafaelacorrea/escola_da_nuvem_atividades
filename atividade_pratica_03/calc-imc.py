peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Peso normal"
elif imc < 30.0:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")