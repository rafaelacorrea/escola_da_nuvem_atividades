valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print("-" * 30)
print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro:.2f}")
print("-" * 30)
print(f"Valor convertido para Dólares: $ {valor_dolar:.2f}")
print(f"Valor convertido para Euros: € {valor_euro:.2f}")