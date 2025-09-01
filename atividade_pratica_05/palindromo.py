import re

def verificar_palindromo(texto):
    texto_limpo = re.sub(r'[^a-zA-Z]', '', texto).lower()

    texto_invertido = texto_limpo[::-1]

    if texto_limpo == texto_invertido:
        return "Sim"
    else:
        return "Não"

print(f"A frase 'Anotaram a data da maratona.' é um palíndromo? {verificar_palindromo('Anotaram a data da maratona.')}")
print(f"A palavra 'Ovo' é um palíndromo? {verificar_palindromo('Ovo')}")
print(f"A frase 'Subi no onibus.' é um palíndromo? {verificar_palindromo('Subi no onibus.')}")
print(f"A palavra 'Python' é um palíndromo? {verificar_palindromo('Python')}")