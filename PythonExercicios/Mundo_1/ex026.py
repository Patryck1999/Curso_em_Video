"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez
"""
frase = str(input("Digite uma frase: \n")).lower().strip()
print("A letra 'a' aparece {} vezes na frase".format(frase.count('a')))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.find('a') + 1))
print("A última letra A apareceu na posição {}".format(frase.rfind('a') + 1))
