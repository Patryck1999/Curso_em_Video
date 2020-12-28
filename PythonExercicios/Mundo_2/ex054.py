"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
"""
from datetime import date
menor = 0
maior = 0
ano_atual = date.today().year
for pessoa in range(1, 8):
    ano_nascimento = int(input("Digite qual ano você nasceu pessoa {}/{}: ".format(pessoa, 7)))
    idade = ano_atual - ano_nascimento
    if idade < 0:
        print("Ano de nascimento invalído")
        break
    elif idade < 21:
        menor += 1
    else:
        maior += 1
print("Existem {} maiores de idade".format(maior))
print("e {} pessoas menores de idade".format(menor))
