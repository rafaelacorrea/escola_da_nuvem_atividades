try:
    preco_original_str = input("Digite o preço original do produto: ")
    percentual_desconto_str = input("Digite o percentual de desconto (ex: 10 para 10%): ")

    preco_original = float(preco_original_str)
    percentual_desconto = float(percentual_desconto_str)

    valor_do_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_do_desconto

    print("\n--- Detalhes da Compra ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto Aplicado: {percentual_desconto}%")
    print(f"Valor do Desconto: R$ {valor_do_desconto:.2f}")
    print(f"Preço Final: R$ {preco_final:.2f}")

except ValueError:
    print("\nErro: Por favor, digite apenas valores numéricos válidos.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")