"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

numero = int(input("Digite um número para descobrir seu sucessor e antecessor: "))
sucessor = numero + 1
antecessor = numero - 1
print("analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(numero, antecessor, sucessor))
