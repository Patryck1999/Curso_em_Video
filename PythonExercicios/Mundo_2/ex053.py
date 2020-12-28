"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
Ex: APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""

"""
frase = ''.join(str(input("Digite uma frase: ").strip()).split())
palindromo = ''.join(frase[::-1].split())
print(frase)
print(palindromo)
if frase == palindromo:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
"""

"""
frase = str(input("Digite uma frase: ").strip())
lista = []

for letra in range(0, len(frase)):
    if frase[letra] != ' ':
        lista.append(frase[letra])
palindromo = ''.join(lista)
if palindromo == palindromo[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
"""
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
print("Você digitou a frase {}".format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
