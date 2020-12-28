"""
Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no
intervalo de 1 até 500.
"""
"""
inicio = 1
final = 500
soma = 0
contador = 0
for numero in range(inicio, final + 1):
    if numero % 2 == 1 and numero % 3 == 0:
        print(numero)
        soma += numero
        contador += 1
print("A soma entre os {} números impares e que são multiplos de três até 500 é: {}".format(contador, soma))
"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))
