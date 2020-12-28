"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cda um dos digitos separados.
Ex:
Digite um número: 1834

Unidade: 4
Dezena: 3
Centena: 8
milhar: 1
"""

numero = int(input("Digite um número de 0 a 9999:"))
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10

print("O numero {} é uma milhar".format(milhar))
print("O numero {} é uma centena".format(centena))
print("O numero {} é uma dezena".format(dezena))
print("O numero {} é uma unidade".format(unidade))



