"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotesusa.
"""
"""
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = ((co ** 2) + (ca ** 2)) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))
"""
from math import hypot

cateto_oposto = float(input("Digite o cateto oposto do triangulo retângulo: "))
cateto_adjacente = float(input("Digite o cateto adjacente do triângulo retângulo: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
