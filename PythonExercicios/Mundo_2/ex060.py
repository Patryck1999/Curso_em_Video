"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
EX: 5! = 5x4x3x2x1 = 120
"""

numero = int(input("Digite o número que você quer saber o fatorial: "))
contador = numero
fatorial = 1
print("Calculando {}! = ".format(numero), end="")
while contador > 0:
    print("{}".format(contador), end='')
    print(" x " if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1
print("{}".format(fatorial), end="")


"""
fatorial = int(input("Digite o número que você quer saber o fatorial: "))
acumulador = 1
for iteracao in range(fatorial, 1, -1):
    acumulador = acumulador * iteracao
print("A fatorial do número {} é {}".format(fatorial, acumulador))
"""
"""
from math import factorial
n = int(input("Digite um número para calcular seu Fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}.".format(n, f))
"""

