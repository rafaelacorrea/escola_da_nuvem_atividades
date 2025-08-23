temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Unidade para converter (C, F ou K): ").upper()
temperatura_convertida = None

if unidade_origem == unidade_destino:
    temperatura_convertida = temperatura
    print(f"\nAs unidades de origem e destino são as mesmas. O valor é {temperatura:.2f}°{unidade_origem}")
elif unidade_origem == 'C':
    if unidade_destino == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura + 273.15
elif unidade_origem == 'F':
    if unidade_destino == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
elif unidade_origem == 'K':
    if unidade_destino == 'C':
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
else:
    print("\nUnidade de origem inválida. Por favor, use C, F ou K.")

if temperatura_convertida is not None:
    print(f"\n{temperatura:.2f}°{unidade_origem} é igual a {temperatura_convertida:.2f}°{unidade_destino}")