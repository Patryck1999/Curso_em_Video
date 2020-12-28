"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas.
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome.
"""

nome = str(input("Digite seu nome completo: \n"))
print("Seu nome em MAIÚSCULO é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome.strip()) - nome.count(' ')))
print("Ou seu nome tem {} letras sem nenhum espaço".format(len(''.join(nome.split()))))
print("Seu primeiro nome {} tem {} letras".format(nome.split()[0], nome.find(' ')))
print("Seu primeiro nome {} tem {} letras".format(nome.split()[0], len(nome.split()[0])))
