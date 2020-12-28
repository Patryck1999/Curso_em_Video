"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
"""
numero = int(input("Digite um número para descobrir se ele é para ou impar: "))

if numero % 2 == 0:
    print("Número {} é par!".format(numero))
else:
    print("Número {} é impar!".format(numero))
