"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan
angulo = float(input("Digite um angulo para calcular o seno, cosseno e tangente: "))
seno = sin(radians(angulo))
print("O ângulo de {:.2f} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {:.2f} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {:.2f} tem a TANGENTE de {:.2f}".format(angulo, tangente))
