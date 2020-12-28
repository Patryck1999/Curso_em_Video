"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA no nome.
"""
nome = str(input("Digite o seu nome:\n").strip().upper())
print("O seu nome {} tem 'SILVA' contido nele? {}".format(nome, "SILVA" in nome))
