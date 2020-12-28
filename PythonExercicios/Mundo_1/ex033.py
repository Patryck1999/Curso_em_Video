"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

"""
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("numero {} é o maior número".format(numero_1))
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("numero {} é o maior número".format(numero_2))
elif numero_3 > numero_1 and numero_3 > numero_2:
    print("numero {} é o maior número".format(numero_3))
else:
    print("Os número são iguais")
"""

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

maior = numero_1
if numero_2 > numero_3 and numero_2 > numero_1:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

menor = numero_1
if numero_2 < numero_3 and numero_2 < numero_1:
    menor = numero_2
if numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
