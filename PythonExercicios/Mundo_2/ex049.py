"""
Refaça o DESAFIO 009, mostre a tabuada de um número que o usuário escolher só que agora utilizando um laço for.
"""

numero = int(input("Digite a tabuada em que você quer saber: "))
inicio = 0
final = 10
print("-" * 15)
for multiplicando in range(inicio, final + 1):
    print("{} x {:2} = {:2}".format(numero, multiplicando, numero * multiplicando))
print("-" * 15)
